# watchexec

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/watchexec/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ansiweather
,
k8sec
,
transmission create
.
watchexec
Run arbitrary commands when files change.
More information:
https://github.com/watchexec/watchexec
.
Call
ls -la
when any file in the current directory changes:
watchexec -- {{ls -la}}
Run
make
when any JavaScript, CSS and HTML files in the current directory change:
watchexec --exts {{js,css,html}} make
Run
make
when any file in the
lib
or
src
subdirectories change:
watchexec --watch {{lib}} --watch {{src}} {{make}}
Call/restart
my_server
when any file in the current directory change, sending
SIGKILL
to stop the child process:
watchexec --restart --signal {{SIGKILL}} {{my_server}}
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
