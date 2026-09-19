# split

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/split/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fping
,
optipng
,
ugrep
,
git verify commit
.
split
Split a file into pieces.
More information:
https://www.gnu.org/software/coreutils/split
.
Split a file, each split having 10 lines (except the last split):
split -l {{10}} {{filename}}
Split a file into 5 files. File is split such that each split has same size (except the last split):
split -n {{5}} {{filename}}
Split a file with 512 bytes in each split (except the last split; use 512k for kilobytes and 512m for megabytes):
split -b {{512}} {{filename}}
Split a file with at most 512 bytes in each split without breaking lines:
split -C {{512}} {{filename}}
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
