# at

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/at/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
buku
,
notmuch
,
julia
,
git archive file
.
at
Execute commands once at a later time.
Service atd (or atrun) should be running for the actual executions.
More information:
https://manned.org/at
.
Execute commands from standard input in 5 minutes (press
Ctrl + D
when done):
at now + 5 minutes
Execute a command from standard input at 10:00 AM today:
echo "{{./make_db_backup.sh}}" | at 1000
Execute commands from a given file next Tuesday:
at -f {{path/to/file}} 9:30 PM Tue
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
