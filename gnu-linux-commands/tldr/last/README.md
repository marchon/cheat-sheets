# last

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/last/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
elm
,
linkchecker
,
hg clone
,
emulator
.
last
View the last logged in users.
More information:
https://manned.org/last
.
View last logins, their duration and other information as read from
/var/log/wtmp
:
last
Specify how many of the last logins to show:
last -n {{login_count}}
Print the full date and time for entries and then display the hostname column last to prevent truncation:
last -F -a
View all logins by a specific user and show the IP address instead of the hostname:
last {{username}} -i
View all recorded reboots (i.e., the last logins of the pseudo user "reboot"):
last reboot
View all recorded shutdowns (i.e., the last logins of the pseudo user "shutdown"):
last shutdown
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
