# leave

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/leave/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xml unescape
,
salt run
,
dlv
,
couchdb
.
leave
Set a reminder for when it's time to leave.
To remove reminders use
kill $(pidof leave)
.
More information:
https://www.freebsd.org/cgi/man.cgi?query=leave
.
Set a reminder at a given time:
leave {{time_to_leave}}
Set a reminder to leave at noon:
leave {{1200}}
Set a reminder in a specific amount of time:
leave +{{amount_of_time}}
Set a reminder to leave in 4 hours and 4 minutes:
leave +{{0404}}
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
