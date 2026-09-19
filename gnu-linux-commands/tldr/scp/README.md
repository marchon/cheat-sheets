# scp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/scp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hg status
,
gopass
,
dcg
,
pwgen
,
hive
.
scp
Secure copy.
Copy files between hosts using Secure Copy Protocol over SSH.
More information:
https://man.openbsd.org/scp
.
Copy a local file to a remote host:
scp {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}
Use a specific port when connecting to the remote host:
scp -P {{port}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}
Copy a file from a remote host to a local directory:
scp {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}
Recursively copy the contents of a directory from a remote host to a local directory:
scp -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}
Copy a file between two remote hosts transferring through the local host:
scp -3 {{host1}}:{{path/to/remote_file}} {{host2}}:{{path/to/remote_directory}}
Use a specific username when connecting to the remote host:
scp {{path/to/local_file}} {{remote_username}}@{{remote_host}}:{{path/to/remote_directory}}
Use a specific ssh private key for authentication with the remote host:
scp -i {{~/.ssh/private_key}} {{local_file}} {{remote_host}}:{{/path/remote_file}}
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
