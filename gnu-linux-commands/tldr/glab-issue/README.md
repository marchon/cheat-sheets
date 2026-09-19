# glab-issue

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/glab-issue/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
salt call
,
mp4box
,
hg update
.
glab issue
Manage GitLab issues from the command-line.
More information:
https://glab.readthedocs.io/en/latest/issue
.
Display a specific issue:
glab issue view {{issue_number}}
Display a specific issue in the default web browser:
glab issue view {{issue_number}} --web
Create a new issue in the default web browser:
glab issue create --web
List the last 10 issues with the
bug
label:
glab issue list --per-page {{10}} --label "{{bug}}"
List closed issues made by a specific user:
glab issue list --closed --author {{username}}
Reopen a specific issue:
glab issue reopen {{issue_number}}
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
