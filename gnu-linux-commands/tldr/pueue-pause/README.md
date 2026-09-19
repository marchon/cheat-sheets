# pueue-pause

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pueue-pause/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
wait
,
transmission create
,
pveperf
.
pueue pause
Pause running tasks or groups.
See also:
pueue start
.
More information:
https://github.com/Nukesor/pueue
.
Pause all tasks in the default group:
pueue pause
Pause a running task:
pueue pause {{task_id}}
Pause a running task and stop all its direct children:
pueue pause --children {{task_id}}
Pause all tasks in a group and prevent it from starting new tasks:
pueue pause --group {{group_name}}
Pause all tasks and prevent all groups from starting new tasks:
pueue pause --all
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
