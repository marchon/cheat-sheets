# sudo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sudo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
su
,
kompose
,
z
,
smalltalkci
,
git difftool
.
sudo
Executes a single command as the superuser or another user.
More information:
https://www.sudo.ws/sudo.html
.
Run a command as the superuser:
sudo {{less /var/log/syslog}}
Edit a file as the superuser with your default editor:
sudo --edit {{/etc/fstab}}
Run a command as another user and/or group:
sudo --user={{user}} --group={{group}} {{id -a}}
Repeat the last command prefixed with
sudo
(only in
bash
,
zsh
, etc.):
sudo !!
Launch the default shell with superuser privileges and run login-specific files (
.profile
,
.bash_profile
, etc.):
sudo --login
Launch the default shell with superuser privileges without changing the environment:
sudo --shell
Launch the default shell as the specified user, loading the user's environment and reading login-specific files (
.profile
,
.bash_profile
, etc.):
sudo --login --user={{user}}
List the allowed (and forbidden) commands for the invoking user:
sudo --list
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
