# gitlab

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gitlab/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tox
,
groups
,
ocamlopt
,
dash
,
go get
.
gitlab
Ruby wrapper and CLI for the GitLab API.
Some subcommands such as
gitlab ctl
have their own usage documentation.
More information:
https://narkoz.github.io/gitlab/
.
Create a new project:
gitlab create_project {{project_name}}
Get info about a specific commit:
gitlab commit {{project_name}} {{commit_hash}}
Get info about jobs in a CI pipeline:
gitlab pipeline_jobs {{project_name}} {{pipeline_id}}
Start a specific CI job:
gitlab job_play {{project_name}} {{job_id}}
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
