# hub

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hub/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
browser sync
,
r2e
,
moe
,
okular
.
hub
A wrapper for Git that adds commands for working with GitHub-based projects.
If set up as instructed by
hub alias
, one can use
git
to run
hub
commands.
More information:
https://hub.github.com
.
Clone a repository using its slug (owners can omit the username):
hub clone {{username}}/{{repo_name}}
Create a fork of the current repository (cloned from another user) under your GitHub profile:
hub fork
Push the current local branch to GitHub and create a PR for it in the original repository:
hub push {{remote_name}} && hub pull-request
Create a PR of the current (already pushed) branch, reusing the message from the first commit:
hub pull-request --no-edit
Create a new branch with the contents of a pull request and switch to it:
hub pr checkout {{pr_number}}
Upload the current (local-only) repository to your GitHub account:
hub create
Fetch Git objects from upstream and update local branches:
hub sync
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
