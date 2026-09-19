# ps

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ps/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mozillavpn
,
at
,
diskonaut
,
xml select
.
ps
Information about running processes.
More information:
https://manned.org/ps
.
List all running processes:
ps aux
List all running processes including the full command string:
ps auxww
Search for a process that matches a string:
ps aux | grep {{string}}
List all processes of the current user in extra full format:
ps --user $(id -u) -F
List all processes of the current user as a tree:
ps --user $(id -u) f
Get the parent PID of a process:
ps -o ppid= -p {{pid}}
Sort processes by memory consumption:
ps --sort size
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
