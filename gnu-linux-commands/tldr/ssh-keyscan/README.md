# ssh-keyscan

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ssh-keyscan/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git delta
,
act
,
ansible
,
gnucash
.
ssh-keyscan
Get the public ssh keys of remote hosts.
More information:
https://man.openbsd.org/ssh-keyscan
.
Retrieve all public ssh keys of a remote host:
ssh-keyscan {{host}}
Retrieve all public ssh keys of a remote host listening on a specific port:
ssh-keyscan -p {{port}} {{host}}
Retrieve certain types of public ssh keys of a remote host:
ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{host}}
Manually update the ssh known_hosts file with the fingerprint of a given host:
ssh-keyscan -H {{host}} >> ~/.ssh/known_hosts
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
