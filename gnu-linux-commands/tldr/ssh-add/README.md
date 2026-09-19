# ssh-add

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ssh-add/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ag
,
mongod
,
vim
,
exercism
,
airmon ng
.
ssh-add
Manage loaded ssh keys in the ssh-agent.
Ensure that ssh-agent is up and running for the keys to be loaded in it.
More information:
https://man.openbsd.org/ssh-add
.
Add the default ssh keys in
~/.ssh
to the ssh-agent:
ssh-add
Add a specific key to the ssh-agent:
ssh-add {{path/to/private_key}}
List fingerprints of currently loaded keys:
ssh-add -l
Delete a key from the ssh-agent:
ssh-add -d {{path/to/private_key}}
Delete all currently loaded keys from the ssh-agent:
ssh-add -D
Add a key to the ssh-agent and the keychain:
ssh-add -K {{path/to/private_key}}
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
