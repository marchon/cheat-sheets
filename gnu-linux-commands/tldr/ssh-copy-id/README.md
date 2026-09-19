# ssh-copy-id

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ssh-copy-id/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
lilypond
,
xxd
,
gh issue
,
dillo
.
ssh-copy-id
Install your public key in a remote machine's authorized_keys.
More information:
https://manned.org/ssh-copy-id
.
Copy your keys to the remote machine:
ssh-copy-id {{username@remote_host}}
Copy the given public key to the remote:
ssh-copy-id -i {{path/to/certificate}} {{username}}@{{remote_host}}
Copy the given public key to the remote with specific port:
ssh-copy-id -i {{path/to/certificate}} -p {{port}} {{username}}@{{remote_host}}
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
