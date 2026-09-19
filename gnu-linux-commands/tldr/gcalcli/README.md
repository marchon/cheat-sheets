# gcalcli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gcalcli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
redshift
,
guacd
,
standard
,
theharvester
.
gcalcli
Command-line tool to interact with Google Calendar.
Requests Google API authorization upon first launch.
More information:
https://github.com/insanum/gcalcli
.
List your events for all your calendars over the next 7 days:
gcalcli agenda
Show events starting from or between specific dates (also takes relative dates e.g. "tomorrow"):
gcalcli agenda {{mm/dd}} [{{mm/dd}}]
List events from a specific calendar:
gcalcli --calendar {{calendar_name}} agenda
Display an ASCII calendar of events by week:
gcalcli calw
Display an ASCII calendar of events for a month:
gcalcli calm
Quick-add an event to your calendar:
gcalcli --calendar {{calendar_name}} quick "{{mm/dd}} {{HH:MM}} {{event_name}}"
Add an event to calendar. Triggers interactive prompt:
gcalcli --calendar "{{calendar_name}}" add
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
