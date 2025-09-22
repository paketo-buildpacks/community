# Paketo Buildpacks Adopters

## Official adopters

Below is a list of organizations and projects that have publicly announced their adoption of Paketo Buildpacks:

<!-- Add an entry for your organization making sure to preserve the alphabetical order -->

| Organization/Project | Description                                                                                                                                                                                                            |
| --- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Bloomberg](https://www.bloomberg.com/company/values/tech-at-bloomberg/open-source/projects/#developer-workflow) | Bloomberg uses Paketo-based buildpacks for its internal platforms.                                                                                                                                                     |
| [Doximity](https://technology.doximity.com/articles/buildpacks-vs-dockerfiles) | Doximity is extending Paketo stacks and using `ruby`, `go` and `nodejs` buildpacks as the foundation of their internal platform                                                                                        |
| [Fly.io](https://fly.io/docs/reference/builders/#buildpacks) | Paketo is one of the buildpacks options that Fly users can select from in `flyctl`. An example using the Go buildpack is available in the [documentation](https://fly.io/docs/getting-started/golang/#inside-fly-toml) | 
| [Greenhouse](https://github.com/grnhse) | Greenhouse uses the Paketo Python and NodeJS buildpacks to drive developer builds within our internal Platform as a Service. Switching to Paketo has been pretty seamless and saved us a ton of work. The support is great and we're able to supplement at times with small downstream buildpacks |
| [Knative](https://knative.dev/) | Paketo buildpacks serve as the default method of converting a Knative function into an OCI container for deployment. The [func CLI](https://github.com/knative-sandbox/kn-plugin-func) uses the pack Go library to programatically invoke a build, potentially applying additional buildpacks when doing so. |
| [Porter](https://docs.porter.run/deploying-applications/deploying-from-github/selecting-application-and-build-method/#customizing-buildpacks)| Porter supports Paketo buildpacks as an option for users to build and deploy their applications on Kubernetes without having to manually containerize them                                                             |
| [Rapid7](https://www.rapid7.com) | Rapid7 uses paketo buildpacks to simplify and standardize container builds for a variety of languages such as java, golang, python, and nodejs. |


## Known adopters

Below is a list of organizations and projects that have NOT publicly announced their adoption of Paketo Buildpacks, but we've noticed they were using them somehow:

| Organization/Project | Description |
| --- |----------------|
| [Microsoft Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/overview)| Uses a mix of Paketo Buildpacks and Azure buildpacks to build users applications |


## Adding your organization to the list of Paketo Buildpacks Adopters
There are two ways to do so:
  * Add a comment to [this Discussion](https://github.com/paketo-buildpacks/feedback/discussions/30) including a brief description of your use case
   OR
  * Open a PR adding yourself to `ADOPTERS.md`
