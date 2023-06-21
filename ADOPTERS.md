# Paketo Buildpacks Adopters

Below is a list of organizations and projects that have publicly adopted Paketo Buildpacks:

<!-- Add an entry for your organization making sure to preserve the alphabetical order -->

| Organization/Project | Description |
| --- | --- |
| [Apcoa](https://urban-hubs.apcoa.com/) | Apcoa urban hubs uses paketo buildpacks for cloud native services to support different mobility needs. We are looking to expand our use of buildpacks with different type of functions and services used in our cloud platform. |
| [Bloomberg](https://www.bloomberg.com/company/values/tech-at-bloomberg/open-source/projects/#developer-workflow) | Bloomberg uses Paketo-based buildpacks for its internal platforms. |
| [Doximity](https://technology.doximity.com/articles/buildpacks-vs-dockerfiles) | Doximity is extending Paketo stacks and using `ruby`, `go` and `nodejs` buildpacks as the foundation of their internal platform|
| [Fly.io](https://fly.io/docs/reference/builders/#buildpacks) | Paketo is one of the buildpacks options that Fly users can select from in `flyctl`. An example using the Go buildpack is available in the [documentation](https://fly.io/docs/getting-started/golang/#inside-fly-toml)  | 
| [Greenhouse](https://github.com/grnhse) | Greenhouse uses the Paketo Python and NodeJS buildpacks to drive developer builds within our internal Platform as a Service. Switching to Paketo has been pretty seamless and saved us a ton of work. The support is great and we're able to supplement at times with small downstream buildpacks|
| [Knative](https://knative.dev/) | Paketo buildpacks serve as the default method of converting a Knative function into an OCI container for deployment. The [func CLI](https://github.com/knative-sandbox/kn-plugin-func) uses the pack Go library to programatically invoke a build, potentially applying additional buildpacks when doing so. |
| [Porter](https://docs.porter.run/deploying-applications/deploying-from-github/selecting-application-and-build-method/#customizing-buildpacks)|Porter supports Paketo buildpacks as an option for users to build and deploy their applications on Kubernetes without having to manually containerize them|
| [Randoli](https://randoli.ca/app-director/) | Randoli's App Director users can choose Paketo buildpacks to containerize their applications and then deploy them to any Kubernetes cluster straight from the UI |
| [VMware](https://hello-tanzu.vmware.com/getting-started-with-tap-devsecops-path-to-prod/) | VMware uses Paketo-based buildpacks as the build phase implementation in several modern application platforms, including Tanzu Application Platform. |

## Adding your organization to the list of Paketo Buildpacks Adopters
There are two ways to do so:
  * Add a comment to [this Discussion](https://github.com/paketo-buildpacks/feedback/discussions/30) including a brief description of your use case
   OR
  * Open a PR adding yourself to `ADOPTERS.md`
