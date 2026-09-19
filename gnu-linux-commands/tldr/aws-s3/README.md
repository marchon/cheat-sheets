# aws-s3

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-s3/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dirsearch
,
histexpand
,
mullvad
.
aws s3
CLI for AWS S3 - provides storage through web services interfaces.
More information:
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html
.
Show files in a bucket:
aws s3 ls {{bucket_name}}
Sync files and directories from local to bucket:
aws s3 sync {{path/to/files}} s3://{{bucket_name}}
Sync files and directories from bucket to local:
aws s3 sync s3://{{bucket_name}} {{path/to/target}}
Sync files and directories with exclusions:
aws s3 sync {{path/to/files}} s3://{{bucket_name}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*
Remove file from bucket:
aws s3 rm s3://{{bucket}}/{{path/to/file}}
Preview changes only:
aws s3 {{any_command}} --dryrun
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
