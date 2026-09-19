# glab-repo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/glab-repo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sshfs
,
b2sum
,
git effort
,
ant
,
ssh
.
glab repo
Work with GitLab repositories on the command-line.
More information:
https://glab.readthedocs.io/en/latest/repo/index.html#synopsis
.
Create a new repository (if the repository name is not set, the default name will be the name of the current directory):
glab repo create {{name}}
Clone a repository:
glab repo clone {{owner}}/{{repository}}
Fork and clone a repository:
glab repo fork {{owner}}/{{repository}} --clone
View a repository in the default web browser:
glab repo view {{owner}}/{{repository}} --web
Search some repositories in the GitLab instance:
glab repo search -s {{search_string}}
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
