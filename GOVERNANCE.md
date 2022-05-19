# Paketo Governance

This document defines the governance structure for the Paketo project. Initial governance RFC can be found [here](https://github.com/paketo-buildpacks/rfcs/blob/main/implemented/0002-governance.md)

## Organizations:

Paketo consists of two github organizations:

- `paketo-buildpacks`
- `paketo-community`

The `paketo-buildpacks` github organization consists of actively supported buildpacks, libraries etc.

The `paketo-community` github organization is designed as a staging ground for acceptance into the officially supported `paketo-buildpacks` org. Promotion from `paketo-community` into `paketo-buildpacks` requires an official [`rfc`](https://github.com/paketo-buildpacks/rfcs).

## Contribution Model:

The paketo contribution model is divided into the following, Subteams & Roles.

- A subteam is a group responsible for some set of repositories in the `paketo-buildpacks` org. This limits the repositories any individual is allowed to take action in.

- Roles are Contributor, Maintainer, And Steering Committee member. This limits what kinds of actions an individual may be allowed to take on a repository. The Contributor and Maintainer roles are scoped to a subteam, while a Steering Committee member is an organization wide role.


### Subteams
Subteams are responsible for maintaining some set of repositories under the `paketo-buildpacks` org. A natural split is into "Language Teams" responsible for maintaining all buildpack & specification changes that pertain to a particular language ecosystem.

Subteams have ownership & voting power over relevant `rfcs`.

Both maintainers, contributors & steering committee members can be members on any number of subteams.

##### Additional Responsibilities:
Each team is additionally responsible for maintaining  relevant documentation at paketo.io.

### Roles

#### Summary

The following table lists the roles we use within the Paketo community. The table describes:

- General responsibilities expected by individuals in each role
- Requirements necessary to join or stay in a given role
- How the role manifests in terms of permissions and privileges.

<table>
  <thead>
    <tr>
    <th>Role</th>
    <th>Responsibilities</th>
    <th>Requirements</th>
    <th>Privileges</th>
    <th>Scope</th>
    </tr>
  </thead>

  <tr>
    <td>(everyone)</td>
    <td>None</td>
    <td>None</td>
    <td>
        <p>Can submit PRs and issues</p>
        <p>Can join CF Slack workspace</p>
        <p>Can take part in community discussions</p>
    </td>
    <td>GitHub Organization</td>
  </tr>  

  <tr>
    <td>Member</td>
    <td>
        <p>Adheres to code of conduct</p>
    </td>
    <td>
        <p>Signed CLA (only for PRs)</p>
    </td>
    <td>
        <p>Can get PRs accepted</p>
    </td>
    <td>GitHub Organization</td>
  </tr>

  <tr>
    <td rowspan="2">Contributor</td>
    <td colspan="4"><i>Inherits from Member Role</i></td>
  </tr>
  <tr>
    <td>
        <p>Regular active contributor in the community</p>
        <p>Triage issues in their subteam</p>
    </td>
    <td>
        <p>Has made multiple contributions to the project</p>
    </td>
    <td>
        <p>Member of the GitHub paketo-buildpacks (and possibly the paketo-community) orgs</p>
        <p>Member of the Paketo Slack workspace</p>
        <p>May review, approve PRs (non-binding), and merge approved PRs.</p>
        <p>May create branches</p>
    </td>
    <td>Paketo Subteam</td>
  </tr>

  <tr>
  <tr>
    <td rowspan="2">Maintainer</td>
    <td colspan="4"><i>Inherits from Contributor Role</i></td>
  </tr>
  <tr>
    <td>
        <p>Review and approve (binding) PRs</p>
        <p>Ensure contributions align with project goals and meet the project's quality standards</p>
        <p>Provide direction and set goals for their subteam</p>
        <p>Mentor new contributors</p>
    </td>
    <td>
        <p>Must be an existing contributor</p>
        <p>Highly experienced and active reviewer and contributor to an area</p>
    </td>
    <td>
        <p>Can merge PRs</p>
        <p>May vote on RFCS that affect their subteams</p>
    </td>
    <td>Paketo Subteam</td>
  </tr>

  <tr>
    <td rowspan="2">Steering Committee</td>
    <td colspan="4"><i>Inherits from Maintainer Role</i></td>
  </tr>
  <tr>
    <td>
        <p>Set priorities and roadmap for the project</p>
        <p>Mentor new contributors and maintainers</p>
        <p>Vote on governace, role, RFCs, and other project-wide changes</p>
    </td>
    <td>
        <p>Must be an existing maintainer</p>
        <p>Highly active maintainer and participant in multiple functional areas</p>
    </td>
    <td>
        <p>Org-wide permissions</p>
    </td>
    <td>Github Org</td>
  </tr>
</table>

#### Everyone
You do not need to be a member of the Paketo team to help. Anyone can help by using and talking about Paketo Buildpacks, participating in discussions, answering questions on Slack/Stack Overflow, opening issues, submitting PRs, etc... All of these are fantastic and welcome contributions to the community.

#### Contributor
Contributors are those who make regular contributions to the project (documentation, code reviews, responding to issues, participation in proposal discussions, contributing code, etc.). 

New contributors may be self-nominated or nominated by existing contributors, and must be elected by a supermajority of that project’s maintainers. Contributors may review and approve PRs (non-binding), merge approved PRs, and create branches.

#### Maintainers
Maintainers are in charge of the day to day maintenance of the team's projects.

They review and approve (binding) PRs, merge PRs, and may vote on RFCS that affect their subteams, ensuring contributions align with project goals and meet the project's quality standards.

New maintainers must already be contributors, must be nominated by an existing maintainer, and must be elected by a supermajority of the current team's maintainers. Likewise, maintainers can be removed by a supermajority of the current team's maintainers or can resign by notifying one of the current team's maintainers.

In extenuating circumstances, i.e. long term absence of a maintainer, steering committee members may act as maintainers of any team in a voting capacity.

#### Steering Committee
The Steering Committee Members are responsible for the direction of the project (roadmap), subteam leadership, the spec, and cross-cutting concerns such as:
- Voting on repo's being added to this org along with affected Maintainers
- Voting on role changes (eg adding new Steering Committee member)
- Voting on updating this document
- Voting on RFCs that impact any of the above responsibilities.


#### Definitions:

**Supermajority**: Greater than or equal to 66%.


