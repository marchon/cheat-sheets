# vcsh

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/vcsh/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git effort
,
osage
,
pnpx
,
aria2c
.
vcsh
Version Control System for the home directory using Git repositories.
More information:
https://github.com/RichiH/vcsh
.
Initialize an (empty) repository:
vcsh init {{repository_name}}
Clone a repository into a custom directory name:
vcsh clone {{git_url}} {{repository_name}}
List all managed repositories:
vcsh list
Execute a Git command on a managed repository:
vcsh {{repository_name}} {{git_command}}
Push/pull all managed repositories to/from remotes:
vcsh {{push|pull}}
Write a custom
.gitignore
file for a managed repository:
vcsh write-gitignore {{repository_name}}
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
