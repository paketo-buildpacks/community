# Style Guide

## Buildpack Design Best Practices
1. Keep `Detect` and `Build` functions as small as possible.
1. Only add a requirement to a buildpack if it's necessary for the buildpack to run.
1. Only add a provision to a buildpack if it actually supplies something for
   itself or a subsequent buildpack to use.

## Testing
1. Please write tests for your contributions to the Paketo project.
1. If your contribution changes or adds to the API of a buildpack, you'll
   likely need to change or add integration tests.
1. If your contribution changes how the `detect` or `build` executables of a
   buildpack work, you'll likely need to change or add unit tests.

## Preferred Code Structures
1. Many Paketo buildpacks are written in Go. If you are contributing Go, please
   write [Effective Go](https://golang.org/doc/effective_go.html).

1. When reviewing Pull Requests, maintainers may refer to these [Common Go Code
   Review Comments](https://github.com/golang/go/wiki/CodeReviewComments).

1. If you're writing in a shell scripting language, keep [this Shell Style
   Guide](https://google.github.io/styleguide/shellguide.html) in mind.
   * In particular, check out the "When to use Shell" section to consider if
     it's time to switch languages.

## Stack choice

Most Paketo buildpacks can be divided into two categories - 

- Dependency/Distribution buildpacks like - [go-dist](https://github.com/paketo-buildpacks/go-dist), [node-engine](https://github.com/paketo-buildpacks/node-engine), [yarn](https://github.com/paketo-buildpacks/yarn), [dep](https://github.com/paketo-buildpacks/dep) etc. which provide tarball distributions which maybe architecture or linux distro specific.
- Configuration/Utility buildpacks like - [procfile](https://github.com/paketo-buildpacks/procfile), [environment-variables](https://github.com/paketo-buildpacks/environment-variables), [go-mod-vendor](https://github.com/paketo-buildpacks/go-mod-vendor), [npm-install](https://github.com/paketo-buildpacks/npm-install) etc. which use distribution buildpacks or are completely standalone.

1. Whenever possible, we should set the most permissive stack id for a buildpack. The Cloud Native Buildpack [spec](https://github.com/buildpacks/spec/blob/buildpack/0.5/buildpack.md#buildpack-implementations) allows for a wildcard stack `*` which indicates compatibility with any stack. 

1. The wildcard stack should be the stack of choice for utility or configuration buildpacks provided they can work on any linux stack. This should be the case for buildpacks written in `go` that are standalone and don't rely on any implicit stack dependencies.

1. If there are cases where a buildpack may work with any stack, but only under certain conditions, the buildpack should still indicate compatibility with any stack via the `*` stack id and dynamically validate the conditions it would properly execute in during its `detect` or `build` step with the aim being to fail as fast as possible if an incompatible environment is detected.