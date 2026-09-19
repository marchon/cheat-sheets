# bfg

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bfg/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
rapper
,
laravel
,
git bundle
,
swig
.
bfg
Remove large files or passwords from Git history like git-filter-branch.
Note: if your repository is connected to a remote, you will need to force push to it.
More information:
https://rtyley.github.io/bfg-repo-cleaner/
.
Remove a file with sensitive data but leave the latest commit untouched:
bfg --delete-files {{file_with_sensitive_data}}
Remove all text mentioned in the specified file wherever it can be found in the repository's history:
bfg --replace-text {{path/to/file.txt}}
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
