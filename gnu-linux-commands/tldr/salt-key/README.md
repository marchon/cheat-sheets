# salt-key

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/salt-key/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dust
,
patch
,
apm
,
javadoc
,
ansible playbook
.
salt-key
Manages salt minion keys on the salt master.
Needs to be run on the salt master, likely as root or with sudo.
More information:
https://docs.saltstack.com/ref/cli/salt-key.html
.
List all accepted, unaccepted and rejected minion keys:
salt-key -L
Accept a minion key by name:
salt-key -a {{MINION_ID}}
Reject a minion key by name:
salt-key -r {{MINION_ID}}
Print fingerprints of all public keys:
salt-key -F
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
