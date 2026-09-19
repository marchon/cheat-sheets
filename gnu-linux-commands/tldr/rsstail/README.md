# rsstail

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rsstail/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
watch
,
blockout2
,
fakedata
,
mosquitto_sub
.
rsstail
tail
for RSS feeds.
More information:
https://github.com/gvalkov/rsstail.py
.
Show the feed of a given URL and wait for new entries appearing at the bottom:
rsstail -u {{url}}
Show the feed in reverse chronological order (newer at the bottom):
rsstail -r -u {{url}}
Include publication date and link:
rsstail -pl -u {{url}}
Set update interval:
rsstail -u {{url}} -i {{interval_in_seconds}}
Show feed and exit:
rsstail -1 -u {{url}}
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
