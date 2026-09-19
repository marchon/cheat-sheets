# pueue-start

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pueue-start/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
make
,
ssh keyscan
,
hg init
,
fio
.
pueue start
Resume operation of specific tasks or groups of tasks.
See also:
pueue pause
.
More information:
https://github.com/Nukesor/pueue
.
Resume all tasks in the default group:
pueue start
Resume a specific task:
pueue start {{task_id}}
Resume multiple tasks at once:
pueue start {{task_id}} {{task_id}}
Resume all tasks and start their children:
pueue start --all --children
Resume all tasks in a specific group:
pueue start group {{group_name}}
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
