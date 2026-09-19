# fly

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fly/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
glab alias
,
tmux
,
base32
,
apktool
.
fly
Command-line tool for concourse-ci.
More information:
https://concourse-ci.org/fly.html
.
Authenticate with and save concourse target:
fly --target {{target_name}} login --team-name {{team_name}} -c {{https://ci.example.com}}
List targets:
fly targets
List pipelines:
fly -t {{target_name}} pipelines
Upload or update a pipeline:
fly -t {{target_name}} set-pipeline --config {{pipeline.yml}} --pipeline {{pipeline_name}}
Unpause pipeline:
fly -t {{target_name}} unpause-pipeline --pipeline {{pipeline_name}}
Show pipeline configuration:
fly -t {{target_name}} get-pipeline --pipeline {{pipeline_name}}
Update local copy of fly:
fly -t {{target_name}} sync
Destroy pipeline:
fly -t {{target_name}} destroy-pipeline --pipeline {{pipeline_name}}
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
