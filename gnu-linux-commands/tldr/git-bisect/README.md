# git-bisect

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-bisect/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git blame someone else
,
hg push
.
git bisect
Use binary search to find the commit that introduced a bug.
Git automatically jumps back and forth in the commit graph to progressively narrow down the faulty commit.
More information:
https://git-scm.com/docs/git-bisect
.
Start a bisect session on a commit range bounded by a known buggy commit, and a known clean (typically older) one:
git bisect start {{bad_commit}} {{good_commit}}
For each commit that
git bisect
selects, mark it as "bad" or "good" after testing it for the issue:
git bisect {{good|bad}}
After
git bisect
pinpoints the faulty commit, end the bisect session and return to the previous branch:
git bisect reset
Skip a commit during a bisect (e.g. one that fails the tests due to a different issue):
git bisect skip
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
