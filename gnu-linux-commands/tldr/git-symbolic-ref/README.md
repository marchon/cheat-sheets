# git-symbolic-ref

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-symbolic-ref/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hunspell
,
tsort
,
protoc
,
zdb
,
xcv
.
git symbolic-ref
Read, change, or delete files that store references.
More information:
https://git-scm.com/docs/git-symbolic-ref
.
Store a reference by a name:
git symbolic-ref refs/{{name}} {{ref}}
Store a reference by name, including a message with a reason for the update:
git symbolic-ref -m "{{message}}" refs/{{name}} refs/heads/{{branch_name}}
Read a reference by name:
git symbolic-ref refs/{{name}}
Delete a reference by name:
git symbolic-ref --delete refs/{{name}}
For scripting, hide errors with
--quiet
and use
--short
to simplify ("refs/heads/X" prints as "X"):
git symbolic-ref --quiet --short refs/{{name}}
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
