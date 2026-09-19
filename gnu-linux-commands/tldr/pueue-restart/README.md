# pueue-restart

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pueue-restart/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
phpbu
,
zopflipng
,
cronic
,
sk
,
p7zip
.
pueue restart
Restart tasks.
More information:
https://github.com/Nukesor/pueue
.
Restart a specific task:
pueue restart {{task_id}}
Restart multiple tasks at once, and start them immediately (do not enqueue):
pueue restart --start-immediately {{task_id}} {{task_id}}
Restart a specific task from a different path:
pueue restart --edit-path {{task_id}}
Edit a command before restarting:
pueue restart --edit {{task_id}}
Restart a task in-place (without enqueuing as a separate task):
pueue restart --in-place {{task_id}}
Restart all failed tasks and stash them:
pueue restart --all-failed --stashed
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
