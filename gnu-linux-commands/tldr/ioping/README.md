# ioping

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ioping/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az bicep
,
yes
,
openssl req
,
ls
.
ioping
Monitor I/O latency in real time.
More information:
https://github.com/koct9i/ioping
.
Show disk I/O latency using the default values and the current directory:
ioping .
Measure latency on /tmp using 10 requests of 1 megabyte each:
ioping -c 10 -s 1M /tmp
Measure disk seek rate on
/dev/sdX
:
ioping -R {{/dev/sdX}}
Measure disk sequential speed on
/dev/sdX
:
ioping -RL {{/dev/sdX}}
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
