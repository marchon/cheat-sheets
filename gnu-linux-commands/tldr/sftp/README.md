# sftp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sftp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sshuttle
,
mk
,
route
,
trawl
,
pip uninstall
.
sftp
Secure File Transfer Program.
Interactive program to copy files between hosts over SSH.
For non-interactive file transfers, see
scp
or
rsync
.
More information:
https://manned.org/sftp
.
Connect to a remote server and enter an interactive command mode:
sftp {{remote_user}}@{{remote_host}}
Connect using an alternate port:
sftp -P {{remote_port}} {{remote_user}}@{{remote_host}}
Connect using a predefined host (in
~/.ssh/config
):
sftp {{host}}
Transfer remote file to the local system:
get {{/path/remote_file}}
Transfer local file to the remote system:
put {{/path/local_file}}
Transfer remote directory to the local system recursively (works with
put
too):
get -R {{/path/remote_directory}}
Get list of files on local machine:
lls
Get list of files on remote machine:
ls
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
