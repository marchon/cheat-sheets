# git-verify-tag

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-verify-tag/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nu
,
jwt
,
exiftool
,
gnomon
,
qmv
,
kops
.
git verify-tag
Check for GPG verification of tags.
If a tag wasn't signed, an error will occur.
More information:
https://git-scm.com/docs/git-verify-tag
.
Check tags for a GPG signature:
git verify-tag {{tag1 optional_tag2 ...}}
Check tags for a GPG signature and show details for each tag:
git verify-tag {{tag1 optional_tag2 ...}} --verbose
Check tags for a GPG signature and print the raw details:
git verify-tag {{tag1 optional_tag2 ...}} --raw
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
