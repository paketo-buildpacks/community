# Paketo Buildpacks Adopters

Below is a list of organizations and projects that have publicly adopted Paketo Buildpacks:

<!-- Add an entry for your organization making sure to preserve the alphabetical order -->

| Organization/Project | Description |
| --- | --- |
| [Bloomberg](https://www.bloomberg.com/company/values/tech-at-bloomberg/open-source/projects/#developer-workflow) | Bloomberg uses Paketo-based buildpacks for its internal platforms. |
| [Fly.io](https://fly.io/docs/reference/builders/#buildpacks) | Paketo is one of the buildpacks options that Fly users can select from in `flyctl`. An example using the Go buildpack is available in the [documentation](https://fly.io/docs/getting-started/golang/#inside-fly-toml)  | 
| [Knative](https://knative.dev/) | Paketo buildpacks serve as the default method of converting a Knative function into an OCI container for deployment. The [func CLI](https://github.com/knative-sandbox/kn-plugin-func) uses the pack Go library to programatically invoke a build, potentially applying additional buildpacks when doing so. |


## Adding your organization to the list of Paketo Buildpacks Adopters
There are two ways to do so:
  * Add a comment to [this Discussion](https://github.com/paketo-buildpacks/feedback/discussions/30) including a brief description of your use case
   OR
  * Open a PR adding yourself to `ADOPTERS.md`
