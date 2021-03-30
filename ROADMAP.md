# Roadmap

The Paketo Buildpacks project is focusing on 3 main themes that encompass our
efforts for 2021: **Solidifying Existing Buildpacks**, **Expanding the
Buildpacks Ecosystem**, and **Non-production Use Cases**.

This roadmap will continue to be updated as our priorities evolve.

## Solidifying Existing Buildpacks

### Python Buildpack Rearchitecture
- Outcomes: A modular and fully-supported Python buildpack.
- RFC: https://github.com/paketo-community/python/blob/main/rfcs/0001-restructure.md
- Issue: [ ] https://github.com/paketo-community/python/issues/226

### PHP Buildpack Rearchitecture
- Outcomes: A modular and fully-supported PHP buildpack.
- RFC: https://github.com/paketo-buildpacks/php/blob/main/rfcs/0001-restructure.md
- Issue: **PENDING**

### Common Configuration via Environment Variables
- Outcomes: All buildpacks are primarily configured via environment variables.
  This will provide a common interface that is maximally configurable for
  different use-cases.
- RFCs:
  - https://github.com/paketo-buildpacks/rfcs/blob/main/accepted/0003-replace-buildpack-yml.md
  - https://github.com/paketo-buildpacks/rfcs/blob/main/accepted/0019-buildpack-set-env-vars-defaults.md
  - https://github.com/paketo-buildpacks/dotnet-core/blob/main/rfcs/0002-buildpack-yml-to-env-var.md
  - https://github.com/paketo-buildpacks/go-build/blob/main/rfcs/0003-buildpack-yml-to-env-var.md
  - https://github.com/paketo-buildpacks/go-dist/blob/main/rfcs/0001-buildpack-yml-to-env-var.md
  - https://github.com/paketo-buildpacks/httpd/blob/main/rfcs/0001-buildpack-yml-to-env-var.md
  - https://github.com/paketo-buildpacks/nginx/blob/main/rfcs/0001-buildpack-yml-to-env-var.md
  - https://github.com/paketo-buildpacks/nodejs/blob/main/rfcs/0003-buildpack-yml-to-env-var.md
  - https://github.com/paketo-buildpacks/ruby/blob/main/rfcs/0003-buildpack-yml-to-env-var.md
- Issues:
  - [ ] https://github.com/paketo-buildpacks/dotnet-core-aspnet/issues/151
  - [ ] https://github.com/paketo-buildpacks/dotnet-core-runtime/issues/150
  - [ ] https://github.com/paketo-buildpacks/dotnet-core-sdk/issues/152
  - [ ] https://github.com/paketo-buildpacks/dotnet-execute/issues/151
  - [ ] https://github.com/paketo-buildpacks/dotnet-publish/issues/154
  - [ ] https://github.com/paketo-buildpacks/httpd/issues/168
  - [ ] https://github.com/paketo-buildpacks/nginx/issues/194
  - [ ] https://github.com/paketo-buildpacks/node-start/issues/58

### Ensure all Language Families include Common Utility Buildpacks
- Outcomes: All language family buildpacks should include the common utility
  buildpacks that enable functionality that is language-ecosystem agnostic.
- RFCs:
  - https://github.com/paketo-buildpacks/ruby/blob/main/rfcs/0002-procfile.md
- Issues:
  - [ ] https://github.com/paketo-buildpacks/dotnet-core/issues/349
  - [ ] https://github.com/paketo-buildpacks/dotnet-core/issues/395
  - [ ] https://github.com/paketo-buildpacks/dotnet-core/issues/6
  - [ ] https://github.com/paketo-buildpacks/dotnet-core/issues/7
  - [ ] https://github.com/paketo-buildpacks/go/issues/326
  - [ ] https://github.com/paketo-buildpacks/go/issues/363
  - [ ] https://github.com/paketo-buildpacks/go/issues/7
  - [ ] https://github.com/paketo-buildpacks/go/issues/8
  - [ ] https://github.com/paketo-buildpacks/nodejs/issues/260
  - [ ] https://github.com/paketo-buildpacks/nodejs/issues/308
  - [ ] https://github.com/paketo-buildpacks/nodejs/issues/7
  - [ ] https://github.com/paketo-buildpacks/nodejs/issues/8
  - [ ] https://github.com/paketo-buildpacks/php/issues/273
  - [ ] https://github.com/paketo-buildpacks/php/issues/315
  - [ ] https://github.com/paketo-buildpacks/php/issues/4
  - [ ] https://github.com/paketo-buildpacks/php/issues/5
  - [ ] https://github.com/paketo-buildpacks/ruby/issues/4
  - [ ] https://github.com/paketo-buildpacks/ruby/issues/511
  - [ ] https://github.com/paketo-buildpacks/ruby/issues/9

### Node.js Buildpack includes APM integrations
- Outcomes: The Node.js buildpack includes integrations that allow for
  application profiling and monitoring on Google Cloud Platform and Azure.
- Issues:
  - [ ] https://github.com/paketo-buildpacks/nodejs/issues/310
  - [ ] https://github.com/paketo-buildpacks/nodejs/issues/311

## Expanding the Buildpacks Ecosystem

### Publish Buildpacks to the CNB Registry
- Outcomes: Registering the Paketo buildpacks in the CNB registry will help to
  make them more discoverable.
- Issue: [ ] https://github.com/paketo-buildpacks/github-config/issues/204

### Host our own Blog
- Outcomes: Hosting our own blog will help to lower the barrier to providing
  high quality buildpacks-related content.
- RFC: https://github.com/paketo-buildpacks/rfcs/blob/main/implemented/0020-blog.md
- Implementation Repository: https://github.com/paketo-buildpacks/blog

### Expose Buildpack Ecosystem Metadata via a Dashboard
- Outcomes: Exposing buildpack metadata in a public location will help with
  transparency and efficiency in delivering buildpack features and bug fixes.
- RFC: https://github.com/paketo-buildpacks/rfcs/blob/main/implemented/0018-dashboard.md
- Implementation Repository: https://github.com/paketo-buildpacks/dashboard

### Distribute Buildpacks via Docker Hub
- Outcomes: Buildpacks are made more discoverable by hosting on the popular
  Docker Hub registry.
- RFC: https://github.com/paketo-buildpacks/rfcs/pull/28
- Pull Request: https://github.com/paketo-buildpacks/github-config/pull/213

### Support HTTP Functions in the Go Buildpack
- Outcomes: A new set of function-based Go applications can be supported.
- RFC: https://github.com/paketo-buildpacks/rfcs/pull/29
- Issue: **PENDING**

### Rust Buildpack
- Outcomes: A new set of Rust applications can be supported.
- RFC: https://github.com/paketo-buildpacks/rfcs/blob/main/accepted/0014-rust.md
- Implementation Repositories:
  - https://github.com/paketo-community/rust
  - https://github.com/paketo-community/rust-dist
  - https://github.com/paketo-community/cargo-install

### Web Server Buildpack
- Outcomes: A new set of Web Server applications can be supported.
- RFC: https://github.com/paketo-buildpacks/rfcs/blob/main/accepted/0006-web-servers.md
- Implementation Repository: https://github.com/paketo-community/web-servers

### Support poetry in Python Buildpack
- Outcomes: Python applications that use the [poetry dependency manager](https://python-poetry.org) can be supported.
- RFC: **PENDING**
- Feature Request: https://github.com/paketo-community/python/issues/196

## Non-Production Use Cases

### Local-Development Framework Integrations
- Outcomes: Buildpacks play a supporting role in enabling a productive local
  development experience.
- Explorations:
  - Tilt: https://github.com/ryanmoran/explorations/blob/main/0002-tilt/README.md
  - Skaffold: https://github.com/ryanmoran/explorations/blob/main/0004-skaffold/README.md
