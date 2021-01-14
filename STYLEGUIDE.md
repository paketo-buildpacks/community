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
