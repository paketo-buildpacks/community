# Roadmap

The Paketo Buildpacks project is focusing on 3 main themes that encompass our
efforts for 2022: **Improving and Expanding our Base Image / Stack / Builder
Offering**, **Improving the Buildpack Authoring Experience**, and
**Improvements to Dependency Management and Caching**.

## Improving and Expanding our Base Image / Stack / Builder Offering

### [RFC0045](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0045-user-ids.md): Secure runtime environments

This RFC recommends that Paketo Buildpacks should in general strive to avoid
making run-time modifications to the Buildpacks layers or the application
directory by default. Instead, they should consider the output image to be
read-only by default and explicitly set the parts that need to be writeable
during runtime.

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/188

### [RFC0046](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0046-image-retention-policy.md): Define an Image & Dependency Retention Policy for Paketo Images

At the moment, the Paketo Project is maintaining images (buildpack, builder,
stack, etc..) and hosted dependencies since the beginning of the project. This
RFC proposes that we define an image and dependency retention policy that would
allow the project to delete old images and dependencies.

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/189

### [stacks/RFC0004](https://github.com/paketo-buildpacks/rfcs/blob/main/text/stacks/0004-jammy-jellyfish.md): Stacks based on Ubuntu 2022.04: Jammy Jellyfish

A set of stacks based on the Ubuntu 2022.04 LTS (Jammy Jellyfish) release base
image should be developed, released, and maintained by the Stacks subteam. Like
the existing Bionic stacks, these new stacks should come in "full", "base", and
"tiny" variants with similar, if not identical, sets of packages pre-installed.

- Tracking Issue: https://github.com/paketo-buildpacks/stacks/issues/133

## Improving the Buildpack Authoring Experience

### [RFC0040](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0040-auto-reference-docs.md): Auto-generate Reference Documentation

We would like to make structural changes to the existing buildpacks
repositories in order to facilitate the generation of automated documentation
for each buildpack on the Paketo website.

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/178

## Improvements to Dependency Management and Caching

### [Exploration](https://github.com/paketo-community/explorations/issues/8): Buildpack Dependency Management Improvements

Many of the Paketo buildpacks contain references to dependencies that they will
install during their build phase. These dependencies are often language
runtimes like Ruby MRI or package managers like Poetry. The dependencies are
tracked and built from their upstream source
([dep-server](https://github.com/paketo-buildpacks/dep-server)) and updated in
buildpacks ([`jam
update-dependencies`](https://github.com/paketo-buildpacks/jam/blob/8d4a1a18bfc2b810e5038e5c496258843a8f2b51/commands/update_dependencies.go)
and [dependency/update
action](https://github.com/paketo-buildpacks/github-config/blob/cfa9081b98d7b8e574461e12e5527ef5d826c7d9/actions/dependency/update/action.yml))
through a considerable amount of automation. This current architecture has
outlived its utility and will likely present a significant technical headwind
as we attempt to move buildpacks to new stacks.

## Other Open RFCs

### [RFC0015](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0015-dockerhub-distribution.md): Distribute Buildpacks via Docker Hub

In addition to the current Google Container Registry (GCR) distribution
channel, buildpacks should be distributed via Docker Hub.

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/62

### [RFC0017](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0017-go-http-fn.md): Support HTTP Functions in the Go Buildpack

A Go buildpack that wraps an `http.HandlerFunc` in appropriate scaffolding to
serve HTTP, and composes nicely with the existing `go-build` buildpacks.

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/63

### [RFC0019](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0019-buildpack-set-env-vars-defaults.md): Default Behaviour for Buildpack-Set Language Ecosystem Environment Variables

Paketo buildpacks sometimes use language ecosystem environment variables to
configure build- and launch time behaviour.  The environment variables' values
can come a) from user input at build/launch time or b) from buildpacks'
"opinions" about proper settings for the container build. If a user provides a
language ecosystem environment variable at build time **and** the buildpack
typically sets an opinionated build time value, the user's value should
override or have precedence over the buildpack-set value. Likewise if a user
provides a language ecosystem environment variable at launch time.

In addition, if a user provides a language-ecosystem environment variable at
build time, that value **should not** be "sticky" -- it should not influence
the launch time value of the environment variable. If a user wants to change
the launch time value of an environment variable, they should provide it at
launch time.

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/64

### [RFC0027](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0027-log-levels.md): Common Logging Levels for Buildpacks

All Paketo buildpacks should provide a mechanism for tuning log verbosity. To
enable this configuration, the buildpacks should respect a `BP_LOG_LEVEL`
environment variable.

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/65

### [RFC0032](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0032-reloadable-process-types.md): Reloadable Process Types

Provide a utility buildpack to support language buildpacks in creating
reloadable process types for their run containers.

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/116

### [RFC0037](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0037-remote-debug.md): Remote Debug

The Java buildpack presently supports enabling remote debugging for
applications. More buildpacks are looking to enable this functionality. It
would be helpful to have a consistent set of environment variables used for
enabling remote connections.

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/175

### [RFC0038](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0038-cdx-syft-sbom.md): Support for CycloneDX and Syft SBoM in Paketo

Buildpacks which directly provide a dependency or buildpacks which install
application dependencies will support the generation of SBoM in the format of
CycloneDX and Syft. Per [CNB
RFC#95](https://github.com/buildpacks/rfcs/blob/main/text/0095-sbom.md), the
SBoM documents will live at `<layer>.bom.<ext>.json`, `launch.bom.<ext>.json`
and `build.bom.<ext>.json` where `<ext>` will be `cdx` (CycloneDX) or
`syft` (Syft).

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/176

### [RFC0044](https://github.com/paketo-buildpacks/rfcs/blob/main/text/0044-disable-sbom.md): Provide Global Mechanism to Disable SBOM Generation

Users should have a mechanism to disable the generation of SBOM documents
during the build process.

- Tracking Issue: https://github.com/paketo-buildpacks/rfcs/issues/180
