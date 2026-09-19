# awslogs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/awslogs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gnuplot
,
virsh pool autostart
.
awslogs
Queries groups, streams and events from Amazon CloudWatch logs.
More information:
https://github.com/jorgebastida/awslogs
.
List log groups:
awslogs groups
List existing streams for the specified group:
awslogs streams {{/var/log/syslog}}
Get logs for any streams in the specified group between 1 and 2 hours ago:
awslogs get {{/var/log/syslog}} --start='{{2h ago}}' --end='{{1h ago}}'
Get logs that match a specific CloudWatch Logs Filter pattern:
awslogs get {{/aws/lambda/my_lambda_group}} --filter-pattern='{{ERROR}}'
Watch logs for any streams in the specified group:
awslogs get {{/var/log/syslog}} ALL --watch
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
