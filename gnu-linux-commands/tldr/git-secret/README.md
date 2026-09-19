# git-secret

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-secret/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sass
,
pueue log
,
ngs
,
core validate commit
.
git secret
Bash tool which stores private data inside a Git repository.
More information:
https://github.com/sobolevn/git-secret
.
Initialize
git-secret
in a local repository:
git secret init
Grant access to the current Git user's email:
git secret tell -m
Grant access by email:
git secret tell {{email}}
Revoke access by email:
git secret killperson {{email}}
List emails with access to secrets:
git secret whoknows
Register a secret file:
git secret add {{path/to/file}}
Encrypt secrets:
git secret hide
Decrypt secret files:
git secret reveal
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
