# influx

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/influx/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pup
,
tex
,
git fame
,
php
,
jhsdb
,
balena
.
influx
InfluxDB command-line client.
More information:
https://docs.influxdata.com/influxdb/v1.7/tools/shell/
.
Connect to an InfluxDB running on localhost with no credentials:
influx
Connect with a specific username (will prompt for a password):
influx -username {{username}} -password ""
Connect to a specific host:
influx -host {{hostname}}
Use a specific database:
influx -database {{database_name}}
Execute a given command:
influx -execute "{{influxql_command}}"
Return output in a specific format:
influx -execute "{{influxql_command}}" -format {{json|csv|column}}
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
