# git-checkout-index

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-checkout-index/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
local
,
tailscale
,
git prune
,
git obliterate
.
git checkout-index
Copy files from the index to the working tree.
More information:
https://git-scm.com/docs/git-checkout-index
.
Restore any files deleted since the last commit:
git checkout-index --all
Restore any files deleted or changed since the last commit:
git checkout-index --all --force
Restore any files changed since the last commit, ignoring any files that were deleted:
git checkout-index --all --force --no-create
Export a copy of the entire tree at the last commit to the specified directory (the trailing slash is important):
git checkout-index --all --force --prefix={{path/to/export_directory/}}
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
