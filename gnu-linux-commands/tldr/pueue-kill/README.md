# pueue-kill

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pueue-kill/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gxl2gv
,
ncdu
,
svn changelist
.
pueue kill
Kill running tasks or whole groups.
More information:
https://github.com/Nukesor/pueue
.
Kill all tasks in the default group:
pueue kill
Kill a specific task:
pueue kill {{task_id}}
Kill a task and terminate all its child processes:
pueue kill --children {{task_id}}
Kill all tasks in a group and pause the group:
pueue kill --group {{group_name}}
Kill all tasks across all groups and pause all groups:
pueue kill --all
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
