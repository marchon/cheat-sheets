# gh-auth

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-auth/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
supervisorctl
,
dvc add
,
gnucash
.
gh auth
Authenticate with a GitHub host from the command-line.
More information:
https://cli.github.com/manual/gh_auth
.
Log in with interactive prompt:
gh auth login
Log in with a token from standard input (created in https://github.com/settings/tokens):
echo {{your_token}} | gh auth login --with-token
Check if you are logged in:
gh auth status
Log out:
gh auth logout
Log in with a specific GitHub Enterprise Server:
gh auth login --hostname {{github.example.com}}
Refresh the session to ensure authentication credentials have the correct minimum scopes (removes additional scopes requested previously):
gh auth refresh
Expand the permission scopes:
gh auth refresh --scopes {{write:org,read:public_key}}
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
