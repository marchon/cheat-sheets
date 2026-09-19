# pkill

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pkill/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
diskonaut
,
puppet
,
doxygen
,
aws s3
.
pkill
Signal process by name.
Mostly used for stopping processes.
More information:
https://www.man7.org/linux/man-pages/man1/pkill.1.html
.
Kill all processes which match:
pkill "{{process_name}}"
Kill all processes which match their full command instead of just the process name:
pkill -f "{{command_name}}"
Force kill matching processes (can't be blocked):
pkill -9 "{{process_name}}"
Send SIGUSR1 signal to processes which match:
pkill -USR1 "{{process_name}}"
Kill the main
firefox
process to close the browser:
pkill --oldest "{{firefox}}"
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
