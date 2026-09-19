# git-submodule

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-submodule/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pg_dump
,
glab release
,
p7zip
.
git submodule
Inspects, updates and manages submodules.
More information:
https://git-scm.com/docs/git-submodule
.
Install a repository's specified submodules:
git submodule update --init --recursive
Add a Git repository as a submodule:
git submodule add {{repository_url}}
Add a Git repository as a submodule at the specified directory:
git submodule add {{repository_url}} {{path/to/directory}}
Update every submodule to its latest commit:
git submodule foreach git pull
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
