# noti

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/noti/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fc list
,
in toto run
,
gh pr create
.
noti
Monitor a process and trigger a banner notification.
More information:
https://github.com/variadico/noti
.
Display a notification when tar finishes compressing files:
noti {{tar -cjf example.tar.bz2 example/}}
Display a notification even when you put it after the command to watch:
{{command_to_watch}}; noti
Monitor a process by PID and trigger a notification when the PID disappears:
noti -w {{process_id}}
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
