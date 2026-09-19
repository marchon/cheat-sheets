# gt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mupdf
,
psql
,
twm
,
gh help
,
man
,
git mailinfo
.
gt
Create and manage sequences of dependent code changes (stacks) for Git and GitHub.
More information:
https://docs.graphite.dev
.
Authenticate the CLI with Graphite's API:
gt auth --token {{graphite_cli_auth_token}}
Initialise
gt
for the repository in the current directory:
gt repo init
Create a new branch stacked on top of the current branch and commit staged changes:
gt branch create {{branch_name}}
Create a new commit and fix upstack branches:
gt commit create -m {{commit_message}}
Force push all branches in the current stack to GitHub and create or update PRs:
gt stack submit
Log all tracked stacks:
gt log short
Print help for a specified subcommand:
gt {{subcommand}} --help
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
