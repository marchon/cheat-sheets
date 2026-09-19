# aws-glue

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-glue/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ffmpeg
,
espanso
,
git annotate
.
aws glue
CLI for AWS Glue.
Defines the public endpoint for the AWS Glue service.
More information:
https://docs.aws.amazon.com/cli/latest/reference/glue/
.
List jobs:
aws glue list-jobs
Start a job:
aws glue start-job-run --job-name {{job_name}}
Start running a workflow:
aws glue start-workflow-run --name {{workflow_name}}
List triggers:
aws glue list-triggers
Start a trigger:
aws glue start-trigger --name {{trigger_name}}
Create a dev endpoint:
aws glue create-dev-endpoint --endpoint-name {{name}} --role-arn {{role_arn_used_by_endpoint}}
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
