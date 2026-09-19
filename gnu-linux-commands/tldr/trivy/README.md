# trivy

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/trivy/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vue build
,
gh alias
,
coffee
,
handbrakecli
.
trivy
Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues.
More information:
https://github.com/aquasecurity/trivy
.
Scan an image:
trivy image {{image:tag}}
Scan the filesystem for vulnerabilities and misconfigurations:
trivy fs --security-checks {{vuln,config}} {{path/to/project_directory}}
Scan a directory for misconfigurations:
trivy config {{path/to/iac_directory}}
Generate output with a SARIF template:
trivy image --format {{template}} --template {{"@sarif.tpl"}} -o {{path/to/report.sarif}} {{image:tag}}
This is a
tldr pages
(
source
, CC BY 4.0) web wrapper for
cheat-sheets.org
.
All commands
,
popular commands
,
most used linux commands
.
Referrals
.
Progressive Web Application (PWA) version to install on your device
.
