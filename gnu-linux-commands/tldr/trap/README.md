# trap

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/trap/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kahlan
,
lldb
,
vegeta
,
oc
,
az feedback
.
trap
Automatically execute commands after receiving signals by processes or the operating system.
Can be used to perform cleanups for interruptions by the user or other actions.
More information:
https://manned.org/trap
.
List available signals to set traps for:
trap -l
List active traps for the current shell:
trap -p
Set a trap to execute commands when one or more signals are detected:
trap 'echo "Caught signal {{SIGHUP}}"' {{SIGHUP}}
Remove active traps:
trap - {{SIGHUP}} {{SIGINT}}
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
