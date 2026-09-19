# git-check-ref-format

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-check-ref-format/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hg pull
,
mullvad
,
vue build
,
git delete branch
.
git check-ref-format
Checks if a given refname is acceptable, and exits with a non-zero status if it is not.
More information:
https://git-scm.com/docs/git-check-ref-format
.
Check the format of the specified refname:
git check-ref-format {{refs/head/refname}}
Print the name of the last branch checked out:
git check-ref-format --branch @{-1}
Normalize a refname:
git check-ref-format --normalize {{refs/head/refname}}
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
