# dvc-checkout

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dvc-checkout/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
psgrep
,
gimp
,
spark
,
iotop
,
virsh list
.
dvc checkout
Checkout data files and directories from cache.
More information:
https://dvc.org/doc/command-reference/checkout
.
Checkout the latest version of all target files and directories:
dvc checkout
Checkout the latest version of a specified target:
dvc checkout {{target}}
Checkout a specific version of a target from a different Git commit/tag/branch:
git checkout {{commit_hash|tag|branch}} {{target}} && dvc checkout {{target}}
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
