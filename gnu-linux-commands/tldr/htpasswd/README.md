# htpasswd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/htpasswd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
grunt
,
gopass
,
uniq
,
maestral
,
type
.
htpasswd
Create and manage htpasswd files to protect web server directories using basic authentication.
More information:
https://httpd.apache.org/docs/current/programs/htpasswd.html
.
Create/overwrite htpasswd file:
htpasswd -c {{path/to/file}} {{username}}
Add user to htpasswd file or update existing user:
htpasswd {{path/to/file}} {{username}}
Add user to htpasswd file in batch mode without an interactive password prompt (for script usage):
htpasswd -b {{path/to/file}} {{username}} {{password}}
Delete user from htpasswd file:
htpasswd -D {{path/to/file}} {{username}}
Verify user password:
htpasswd -v {{path/to/file}} {{username}}
Display a string with username (plain text) and password (md5):
htpasswd -nbm {{username}} {{password}}
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
