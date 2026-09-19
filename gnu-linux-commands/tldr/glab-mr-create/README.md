# glab-mr-create

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/glab-mr-create/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dict
,
sshfs
,
factor
,
tlmgr info
.
glab mr create
Manage GitLab merge requests from the command-line.
More information:
https://glab.readthedocs.io/en/latest/mr/create.html
.
Interactively create a merge request:
glab mr create
Create a merge request, determining the title and description from the commit messages of the current branch:
glab mr create --fill
Create a draft merge request:
glab mr create --draft
Create a merge request specifying the target branch, title, and description:
glab mr create --target-branch {{target_branch}} --title "{{title}}" --description "{{description}}"
Start opening a merge request in the default web browser:
glab mr create --web
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
