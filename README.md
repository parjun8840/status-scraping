
## This utility application scrapes the [GitHub status page](https://www.githubstatus.com/) and reports metrics based on the current status of "GitHub Actions" API
### The below gauge metric is generated when the Actions Jobs status is "Operational"
>##### #HELP ActionsStatus Fetching status from GitHub Page
>##### #TYPE ActionsStatus gauge
>ActionsStatus{actions="Operational"} 1.0

### The below gauge metric is generated when the Actions Jobs status is other than "Operational"
>##### #HELP ActionsStatus Fetching status from GitHub Page
>##### #TYPE ActionsStatus gauge
>ActionsStatus{actions="Operational"} 0.0
