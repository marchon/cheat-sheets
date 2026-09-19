# git-stripspace

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-stripspace/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pdfposter
,
dvc add
,
inkmake
,
home manager
.
git stripspace
Read text (e.g. commit messages, notes, tags, and branch descriptions) from the standard input and clean it into the manner used by Git.
More information:
https://git-scm.com/docs/git-stripspace
.
Trim whitespace from a file:
cat {{path/to/file}} | git stripspace
Trim whitespace and Git comments from a file:
cat {{path/to/file}} | git stripspace --strip-comments
Convert all lines in a file into Git comments:
git stripspace --comment-lines < {{path/to/file}}
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
