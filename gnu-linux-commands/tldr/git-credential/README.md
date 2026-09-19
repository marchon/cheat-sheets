# git-credential

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-credential/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
postcss
,
ssh add
,
chsh
,
thunderbird
.
git credential
Retrieve and store user credentials.
More information:
https://git-scm.com/docs/git-credential
.
Display credential information, retrieving the username and password from configuration files:
echo "{{url=http://example.com}}" | git credential fill
Send credential information to all configured credential helpers to store for later use:
echo "{{url=http://example.com}}" | git credential approve
Erase the specified credential information from all the configured credential helpers:
echo "{{url=http://example.com}}" | git credential reject
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
