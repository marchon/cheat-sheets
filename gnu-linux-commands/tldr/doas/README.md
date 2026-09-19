# doas

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/doas/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git status
,
aws cur
,
john
,
avrdude
.
doas
Executes a command as another user.
More information:
https://man.openbsd.org/doas
.
Run a command as root:
doas {{command}}
Run a command as another user:
doas -u {{user}} {{command}}
Launch the default shell as root:
doas -s
Parse a config file and check if the execution of a command as another user is allowed:
doas -C {{config_file}} {{command}}
Make
doas
request a password even after it was supplied earlier:
doas -L
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
