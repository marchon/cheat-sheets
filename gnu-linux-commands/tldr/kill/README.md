# kill

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kill/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az term
,
glib compile resources
.
kill
Sends a signal to a process, usually related to stopping the process.
All signals except for SIGKILL and SIGSTOP can be intercepted by the process to perform a clean exit.
More information:
https://manned.org/kill
.
Terminate a program using the default SIGTERM (terminate) signal:
kill {{process_id}}
List available signal names (to be used without the
SIG
prefix):
kill -l
Terminate a background job:
kill %{{job_id}}
Terminate a program using the SIGHUP (hang up) signal. Many daemons will reload instead of terminating:
kill -{{1|HUP}} {{process_id}}
Terminate a program using the SIGINT (interrupt) signal. This is typically initiated by the user pressing
Ctrl + C
:
kill -{{2|INT}} {{process_id}}
Signal the operating system to immediately terminate a program (which gets no chance to capture the signal):
kill -{{9|KILL}} {{process_id}}
Signal the operating system to pause a program until a SIGCONT ("continue") signal is received:
kill -{{17|STOP}} {{process_id}}
Send a
SIGUSR1
signal to all processes with the given GID (group id):
kill -{{SIGUSR1}} -{{group_id}}
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
