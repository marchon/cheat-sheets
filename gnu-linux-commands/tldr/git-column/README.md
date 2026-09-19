# git-column

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-column/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mytop
,
ss local
,
starship
,
rvm
.
git column
Display data in columns.
More information:
https://git-scm.com/docs/git-column
.
Format the standard input as multiple columns:
ls | git column --mode={{column}}
Format the standard input as multiple columns with a maximum width of
100
:
ls | git column --mode=column --width={{100}}
Format the standard input as multiple columns with a maximum padding of
30
:
ls | git column --mode=column --padding={{30}}
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
