# git-filter-repo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-filter-repo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nudoku
,
peerflix
,
sops
,
sccmap
.
git filter-repo
A versatile tool for rewriting Git history.
See also:
bfg
.
More information:
https://github.com/newren/git-filter-repo
.
Replace a sensitive string in all files:
git filter-repo --replace-text <(echo '{{find}}==>{{replacement}}')
Extract a single folder, keeping history:
git-filter-repo --path {{path/to/folder}}
Remove a single folder, keeping history:
git-filter-repo --path {{path/to/folder}} --invert-paths
Move everything from sub-folder one level up:
git-filter-repo --path-rename {{path/to/folder/:}}
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
