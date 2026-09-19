# timeout

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/timeout/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
clockwork cli
,
sshpass
,
mutagen
.
timeout
Run a command with a time limit.
More information:
https://www.gnu.org/software/coreutils/timeout
.
Run
sleep 10
and terminate it, if it runs for more than 3 seconds:
timeout {{3s}} {{sleep 10}}
Specify the signal to be sent to the command after the time limit expires. (By default, TERM is sent):
timeout --signal {{INT}} {{5s}} {{sleep 10}}
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
