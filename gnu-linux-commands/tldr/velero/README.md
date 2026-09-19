# velero

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/velero/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az storage
,
az bicep
,
sshuttle
.
velero
Backup and migrate Kubernetes applications and their persistent volumes.
More information:
https://github.com/heptio/velero
.
Create a backup containing all resources:
velero backup create {{backup_name}}
List all backups:
velero backup get
Delete a backup:
velero backup delete {{backup_name}}
Create a weekly backup, each living for 90 days (2160 hours):
velero schedule create {{schedule_name}} --schedules="{{@every 7d}}" --ttl {{2160h0m0s}}
Create a restore from the latest successful backup triggered by specific schedule:
velero restore create --from-schedule {{schedule_name}}
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
