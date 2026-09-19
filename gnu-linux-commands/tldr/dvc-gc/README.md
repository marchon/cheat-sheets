# dvc-gc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dvc-gc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
netlify
,
groff
,
odps table
,
gh pr create
.
dvc gc
Remove unused files and directories from the cache or remote storage.
More information:
https://dvc.org/doc/command-reference/gc
.
Garbage collect from the cache, keeping only versions referenced by the current workspace:
dvc gc --workspace
Garbage collect from the cache, keeping only versions referenced by branch, tags, and commits:
dvc gc --all-branches --all-tags --all-commits
Garbage collect from the cache, including the default cloud remote storage (if set):
dvc gc --all-commits --cloud
Garbage collect from the cache, including a specific cloud remote storage:
dvc gc --all-commits --cloud --remote {{remote_name}}
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
