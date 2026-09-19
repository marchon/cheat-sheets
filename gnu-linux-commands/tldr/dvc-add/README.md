# dvc-add

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dvc-add/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git config
,
composer
,
cloudflared
.
dvc add
Add changed files to the index.
More information:
https://dvc.org/doc/command-reference/add
.
Add a single target file to the index:
dvc add {{path/to/file}}
Add a target directory to the index:
dvc add {{path/to/directory}}
Recursively add all the files in a given target directory:
dvc add --recursive {{path/to/directory}}
Add a target file with a custom
.dvc
filename:
dvc add --file {{custom_name.dvc}} {{path/to/file}}
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
