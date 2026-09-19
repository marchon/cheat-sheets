# logger

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/logger/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
adguardhome
,
unar
,
nomad
,
pve firewall
.
logger
Add messages to syslog (/var/log/syslog).
More information:
https://manned.org/logger
.
Log a message to syslog:
logger {{message}}
Take input from stdin and log to syslog:
echo {{log_entry}} | logger
Send the output to a remote syslog server running at a given port. Default port is 514:
echo {{log_entry}} | logger --server {{hostname}} --port {{port}}
Use a specific tag for every line logged. Default is the name of logged in user:
echo {{log_entry}} | logger --tag {{tag}}
Log messages with a given priority. Default is
user.notice
. See
man logger
for all priority options:
echo {{log_entry}} | logger --priority {{user.warning}}
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
