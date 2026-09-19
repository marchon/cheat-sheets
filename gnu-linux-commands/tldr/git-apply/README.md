# git-apply

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-apply/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kafkacat
,
git reset file
,
hping
.
git apply
Apply a patch to files and/or to the index.
More information:
https://git-scm.com/docs/git-apply
.
Print messages about the patched files:
git apply --verbose {{path/to/file}}
Apply and add the patched files to the index:
git apply --index {{path/to/file}}
Apply a remote patch file:
curl {{https://example.com/file.patch}} | git apply
Output diffstat for the input and apply the patch:
git apply --stat --apply {{path/to/file}}
Apply the patch in reverse:
git apply --reverse {{path/to/file}}
Store the patch result in the index without modifying the working tree:
git apply --cache {{path/to/file}}
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
