# gh-issue

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-issue/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
http server upload
,
go list
.
gh issue
Manage GitHub issues from the command-line.
More information:
https://cli.github.com/manual/gh_issue
.
Display a specific issue:
gh issue view {{issue_number}}
Display a specific issue in the default web browser:
gh issue view {{issue_number}} --web
Create a new issue in the default web browser:
gh issue create --web
List the last 10 issues with the
bug
label:
gh issue list --limit {{10}} --label "{{bug}}"
List closed issues made by a specific user:
gh issue list --state closed --author {{username}}
Display the status of issues relevant to the user, in a specific repository:
gh issue status --repo {{owner}}/{{repository}}
Reopen a specific issue:
gh issue reopen {{issue_number}}
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
