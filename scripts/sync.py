#!/usr/bin/env python3
"""
sync.py — Synchronize TEAMS.md with GitHub Teams in the paketo-buildpacks org.

TEAMS.md is the source of truth. This script computes the diff between what
TEAMS.md says (active members only, excluding Emeritus sections) and what
GitHub currently has, then optionally applies the changes.

Usage:
    python sync.py [--apply] [--file PATH]

    --apply       Apply changes. Without this flag only a dry-run diff is shown.
    --file PATH   Use a local TEAMS.md file instead of fetching it from GitHub.
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.request
from dataclasses import dataclass, field

ORG = "paketo-buildpacks"
TEAMS_MD_URL = (
    "https://raw.githubusercontent.com/paketo-buildpacks/community"
    "/refs/heads/main/TEAMS.md"
)

# These accounts are automation bots. They are always preserved in whatever
# teams they happen to be in — sync never adds or removes them.
BOT_ACCOUNTS = frozenset({"paketo-bot", "paketo-bot-reviewer"})

# Accounts that are the same person under a different GitHub login.
# They are silently ignored during sync (treated as absent).
IGNORED_ACCOUNTS = frozenset({"loewenstein-sap"})

# Maps the subteam heading in TEAMS.md (the "### … Team" text) to the
# corresponding GitHub team slug. The Maintainers and Contributors child-teams
# are derived by appending "-maintainers" / "-contributors".
TEAM_SLUG_MAP: dict[str, str] = {
    "App Monitoring Team": "app-monitoring",
    "Builders Team": "builders",
    "Content Team": "content",
    "Dependencies Team": "dependencies",
    "Go Team": "go",
    "Java Team": "java",
    ".NET Core Team": "dotnet-core",
    "Node.js Team": "nodejs",
    "PHP Team": "php",
    "Python Team": "python",
    "Ruby Team": "ruby",
    "Rust Team": "rust",
    "Stacks Team": "stacks",
    "Tooling Team": "tooling",
    "Utilities Team": "utilities",
    "Web Servers Team": "web-servers",
}


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class SubteamSpec:
    name: str
    slug: str  # GitHub parent-team slug
    maintainers: set = field(default_factory=set)
    contributors: set = field(default_factory=set)


# ---------------------------------------------------------------------------
# TEAMS.md parser
# ---------------------------------------------------------------------------


def _extract_usernames(line: str) -> set[str]:
    """
    Pull GitHub handles from a member line such as:
        [@dmikusa][@dmikusa], [@loewenstein][@loewenstein]
    Each handle appears twice in the reference-link syntax; using a set
    automatically deduplicates them.
    """
    return set(re.findall(r"\[@([^\]]+)\]", line))


def parse_teams_md(content: str) -> tuple[set[str], list[SubteamSpec], set[str]]:
    """
    Parse TEAMS.md and return:
        steering_members  – active Steering Committee members
        subteams          – list of SubteamSpec (active members only)
        all_known_users   – every username ever mentioned in the file
                            (used to detect truly unknown GitHub members)
    """
    lines = content.splitlines()

    # Collect every username from the reference-link block at the bottom.
    # Format: [@username]: https://github.com/username
    all_known_users: set[str] = set()
    for line in lines:
        m = re.match(r"^\[@([^\]]+)\]:\s+https://github\.com/", line.strip())
        if m:
            all_known_users.add(m.group(1))

    steering_members: set[str] = set()
    subteams: list[SubteamSpec] = []

    # Parser state
    section = None  # 'steering' | 'subteams' | None
    in_emeritus = False
    current_team: SubteamSpec | None = None
    current_role: str | None = None  # 'maintainers' | 'contributors'

    for line in lines:
        s = line.strip()

        # ── Top-level section boundaries ────────────────────────────────────
        if s == "## Steering Committee":
            section = "steering"
            in_emeritus = False
            continue

        if s == "## Subteams":
            section = "subteams"
            in_emeritus = False
            current_team = None
            current_role = None
            continue

        # ── Steering Committee section ───────────────────────────────────────
        if section == "steering":
            if s == "### Emeritus Members":
                in_emeritus = True
            elif not in_emeritus and s.startswith("[@"):
                steering_members |= _extract_usernames(s)
            continue

        # ── Subteams section ─────────────────────────────────────────────────
        if section != "subteams":
            continue

        # Team heading:  ### Some Name Team
        if s.startswith("### "):
            team_name = s[4:].strip()
            slug = TEAM_SLUG_MAP.get(team_name)
            if slug is None:
                print(
                    f"WARNING: Unknown team name '{team_name}' in TEAMS.md — skipping",
                    file=sys.stderr,
                )
                current_team = None
            else:
                current_team = SubteamSpec(name=team_name, slug=slug)
                subteams.append(current_team)
            current_role = None
            in_emeritus = False
            continue

        if current_team is None:
            continue

        if s == "#### Maintainers":
            current_role = "maintainers"
            in_emeritus = False
            continue

        if s == "#### Contributors":
            current_role = "contributors"
            in_emeritus = False
            continue

        if s == "##### Emeritus Members":
            in_emeritus = True
            continue

        # Team separator
        if s == "---":
            current_team = None
            current_role = None
            in_emeritus = False
            continue

        # Member line (only when not in an Emeritus block)
        if not in_emeritus and current_role and s.startswith("[@"):
            names = _extract_usernames(s)
            if current_role == "maintainers":
                current_team.maintainers |= names
            else:
                current_team.contributors |= names

    return steering_members, subteams, all_known_users


# ---------------------------------------------------------------------------
# GitHub API helpers (all via the `gh` CLI)
# ---------------------------------------------------------------------------


def _run_gh(args: list[str], *, allow_empty: bool = False) -> str:
    result = subprocess.run(["gh"] + args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: gh {' '.join(args)}\n{result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    return result.stdout


def get_team_members(slug: str) -> set[str]:
    raw = _run_gh(["api", "--paginate", f"orgs/{ORG}/teams/{slug}/members"])
    return {m["login"] for m in json.loads(raw)}


def add_member(slug: str, username: str) -> None:
    _run_gh(
        [
            "api",
            "--method",
            "PUT",
            f"orgs/{ORG}/teams/{slug}/memberships/{username}",
            "-f",
            "role=member",
        ]
    )


def remove_member(slug: str, username: str) -> None:
    _run_gh(
        [
            "api",
            "--method",
            "DELETE",
            f"orgs/{ORG}/teams/{slug}/memberships/{username}",
        ],
        allow_empty=True,
    )


# ---------------------------------------------------------------------------
# Diff computation
# ---------------------------------------------------------------------------


@dataclass
class TeamDiff:
    slug: str
    to_add: set[str]
    to_remove: set[str]
    unknown: list[str]  # in GitHub but not mentioned anywhere in TEAMS.md

    @property
    def has_changes(self) -> bool:
        return bool(self.to_add or self.to_remove)

    @property
    def has_unknown(self) -> bool:
        return bool(self.unknown)


def compute_diff(slug: str, desired: set[str], all_known: set[str]) -> TeamDiff:
    current = get_team_members(slug)

    # Accounts we never touch
    managed = current - BOT_ACCOUNTS - IGNORED_ACCOUNTS

    to_add = desired - managed
    excess = managed - desired

    # Split excess into "mentioned in TEAMS.md (emeritus, etc.) → remove"
    # vs "never mentioned → unknown → fail"
    unknown = [u for u in excess if u not in all_known]
    to_remove = excess - set(unknown)

    return TeamDiff(slug=slug, to_add=to_add, to_remove=to_remove, unknown=unknown)


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------


def print_diff(diff: TeamDiff) -> None:
    if diff.has_changes:
        print(f"  [{diff.slug}]")
        for u in sorted(diff.to_add):
            print(f"    + {u}")
        for u in sorted(diff.to_remove):
            print(f"    - {u}")
    else:
        print(f"  [{diff.slug}] (up to date)")


def apply_diff(diff: TeamDiff) -> None:
    for u in sorted(diff.to_add):
        add_member(diff.slug, u)
        print(f"    Added   {u} → {diff.slug}")
    for u in sorted(diff.to_remove):
        remove_member(diff.slug, u)
        print(f"    Removed {u} ← {diff.slug}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync TEAMS.md → GitHub Teams for paketo-buildpacks"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply the computed changes. Without this flag the script is a dry run.",
    )
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="Path to a local TEAMS.md (default: fetch from GitHub)",
    )
    args = parser.parse_args()

    # ── Load TEAMS.md ────────────────────────────────────────────────────────
    if args.file:
        with open(args.file) as f:
            content = f.read()
        print(f"Using local file: {args.file}\n")
    else:
        print(f"Fetching TEAMS.md …")
        with urllib.request.urlopen(TEAMS_MD_URL) as resp:
            content = resp.read().decode()
        print()

    # ── Parse ────────────────────────────────────────────────────────────────
    steering_members, subteams, all_known_users = parse_teams_md(content)

    print(
        f"Parsed TEAMS.md: {len(steering_members)} active steering members, "
        f"{len(subteams)} subteams, {len(all_known_users)} total known users\n"
    )

    if not args.apply:
        print("DRY RUN — pass --apply to make changes.\n")

    # ── Compute all diffs (read-only pass) ───────────────────────────────────
    all_diffs: list[TeamDiff] = []

    print("Steering Committee:")
    diff = compute_diff("steering-committee", steering_members, all_known_users)
    all_diffs.append(diff)
    print_diff(diff)
    print()

    print("Subteams:")
    for team in subteams:
        for role, desired in [
            ("maintainers", team.maintainers),
            ("contributors", team.contributors),
        ]:
            gh_slug = f"{team.slug}-{role}"
            diff = compute_diff(gh_slug, desired, all_known_users)
            all_diffs.append(diff)
            print_diff(diff)
    print()

    # ── Check for unknown accounts ───────────────────────────────────────────
    errors: list[str] = []
    for diff in all_diffs:
        for u in diff.unknown:
            errors.append(
                f"  [{diff.slug}] '{u}' is present in the GitHub team but is not "
                f"mentioned anywhere in TEAMS.md (not active, not emeritus)."
            )

    if errors:
        print("FATAL: Unexpected accounts found in GitHub teams:", file=sys.stderr)
        for err in errors:
            print(err, file=sys.stderr)
        print(
            "\nPlease update TEAMS.md to account for these users "
            "(add them as active or emeritus members), then re-run.",
            file=sys.stderr,
        )
        sys.exit(1)

    # ── Summary / apply ──────────────────────────────────────────────────────
    has_changes = any(d.has_changes for d in all_diffs)

    if not has_changes:
        print("All teams are up to date.")
        return

    if not args.apply:
        print("Dry run complete. Use --apply to apply the changes above.")
        return

    print("Applying changes …\n")
    for diff in all_diffs:
        if diff.has_changes:
            apply_diff(diff)
    print("\nSync complete.")


if __name__ == "__main__":
    main()
