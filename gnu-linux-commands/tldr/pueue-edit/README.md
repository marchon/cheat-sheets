# pueue-edit

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pueue-edit/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
samtools
,
git push
,
rg
,
sort
,
git reauthor
.
pueue edit
Edit the command or path of a stashed or queued task.
More information:
https://github.com/Nukesor/pueue
.
Edit a task, see
pueue status
to get the task ID:
pueue edit {{task_id}}
Edit the path from which a task is executed:
pueue edit {{task_id}} --path
Edit a command with the specified editor:
EDITOR={{nano}} pueue edit {{task_id}}
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
