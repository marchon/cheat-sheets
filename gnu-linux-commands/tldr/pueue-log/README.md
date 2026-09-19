# pueue-log

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pueue-log/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bat
,
mktemp
,
source
,
gacutil
,
dotnet restore
.
pueue log
Display the log output of 1 or more tasks.
See also:
pueue status
.
More information:
https://github.com/Nukesor/pueue
.
Show the last few lines of output from all tasks:
pueue log
Show the full output of a task:
pueue log {{task_id}}
Show the last few lines of output from several tasks:
pueue log {{task_id}} {{task_id}}
Print a specific number of lines from the tail of output:
pueue log --lines {{number_of_lines}} {{task_id}}
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
