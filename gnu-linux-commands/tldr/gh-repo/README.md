# gh-repo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-repo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
shasum
,
loc
,
indent
,
ifconfig
,
scrcpy
.
gh repo
Work with GitHub repositories on the command-line.
More information:
https://cli.github.com/manual/gh_repo
.
Create a new repository (if the repository name is not set, the default name will be the name of the current directory):
gh repo create {{name}}
Clone a repository:
gh repo clone {{owner}}/{{repository}}
Fork and clone a repository:
gh repo fork {{owner}}/{{repository}} --clone
View a repository in the default web browser:
gh repo view {{repository}} --web
List repositories owned by a specific user or organization (if the owner is not set, the default owner will be the currently logged in user):
gh repo list {{owner}}
List only non-forks repositories:
gh repo list {{owner}} --non-forks
List repositories with a specific primary coding language:
gh repo list {{owner}} --language {{language_name}}
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
