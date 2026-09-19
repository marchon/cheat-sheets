# doctl-auth

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/doctl-auth/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git annex
,
tokei
,
sudo
,
conan
,
swagger codegen
.
doctl auth
Authenticate doctl with one or more API tokens.
More information:
https://docs.digitalocean.com/reference/doctl/reference/auth/
.
Open a prompt to enter an API token and label its context:
doctl auth init --context {{token_label}}
List authentication contexts (API tokens):
doctl auth list
Switch contexts (API tokens):
doctl auth switch --context {{token_label}}
Remove a stored authentication context (API token):
doctl auth remove --context {{token_label}}
Show available commands:
doctl auth --help
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
