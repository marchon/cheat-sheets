# killall

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/killall/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mongoimport
,
tmpmail
,
aws lambda
.
killall
Send kill signal to all instances of a process by name (must be exact name).
All signals except SIGKILL and SIGSTOP can be intercepted by the process, allowing a clean exit.
More information:
https://manned.org/killall
.
Terminate a process using the default SIGTERM (terminate) signal:
killall {{process_name}}
List available signal names (to be used without the 'SIG' prefix):
killall --list
Interactively ask for confirmation before termination:
killall -i {{process_name}}
Terminate a process using the SIGINT (interrupt) signal, which is the same signal sent by pressing
Ctrl + C
:
killall -INT {{process_name}}
Force kill a process:
killall -KILL {{process_name}}
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
