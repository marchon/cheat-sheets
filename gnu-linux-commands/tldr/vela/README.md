# vela

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/vela/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
img2pdf
,
py spy
,
exrex
,
newman
.
vela
Command-line tools for the Vela pipeline.
More information:
https://go-vela.github.io/docs/reference/cli/
.
Trigger a pipeline to run from a Git branch, commit or tag:
vela add deployment --org {{organization}} --repo {{repository_name}} --target {{environment}} --ref {{branch|commit|refs/tags/git_tag}} --description "{{deploy_description}}"
List deployments for a repository:
vela get deployment --org {{organization}} --repo {{repository_name}}
Inspect a specific deployment:
vela view deployment --org {{organization}} --repo {{repository_name}} --deployment {{deployment_number}}
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
