# git-standup

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-standup/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
influx
,
home manager
,
aria2
,
chromium
.
git standup
See commits from a specified user.
Part of
git-extras
.
More information:
https://github.com/tj/git-extras/blob/master/Commands.md#git-standup
.
Show a given author's commits from the last 10 days:
git standup -a {{name|email}} -d {{10}}
Show a given author's commits from the last 10 days and whether they are GPG signed:
git standup -a {[name|email}} -d {{10}} -g
Show all the commits from all contributors for the last 10 days:
git standup -a all -d {{10}}
Display help:
git standup -h
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
