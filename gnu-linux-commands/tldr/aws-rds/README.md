# aws-rds

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-rds/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
svgcleaner
,
clojure
,
mplayer
.
aws rds
CLI for AWS Relational Database Service.
Create and manage relational databases.
More information:
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html
.
Show help for specific RDS subcommand:
aws rds {{subcommand}} help
Stop instance:
aws rds stop-db-instance --db-instance-identifier {{instance_identifier}}
Start instance:
aws rds start-db-instance --db-instance-identifier {{instance_identifier}}
Modify an RDS instance:
aws rds modify-db-instance --db-instance-identifier {{instance_identifier}} {{parameters}} --apply-immediately
Apply updates to an RDS instance:
aws rds apply-pending-maintenance-action --resource-identifier {{database_arn}} --apply-action {{system-update}} --opt-in-type {{immediate}}
Change an instance identifier:
aws rds modify-db-instance --db-instance-identifier {{old_instance_identifier}} --new-db-instance-identifier {{new_instance_identifier}}
Reboot an instance:
aws rds reboot-db-instance --db-instance-identifier {{instance_identifier}}
Delete an instance:
aws rds delete-db-instance --db-instance-identifier {{instance_identifier}} --final-db-snapshot-identifier {{snapshot_identifier}} --delete-automated-backups
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
