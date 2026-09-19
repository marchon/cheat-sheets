# aws

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dolt commit
,
tig
,
dvc add
,
csvstat
.
aws
The official CLI tool for Amazon Web Services.
Some subcommands such as
aws s3
have their own usage documentation.
More information:
https://aws.amazon.com/cli
.
Configure the AWS Command-line:
aws configure wizard
Configure the AWS Command-line using SSO:
aws configure sso
See help text for the AWS command:
aws {{command}} help
Get the caller identity (used to troubleshoot permissions):
aws sts get-caller-identity
List AWS resources in a region and output in YAML:
aws dynamodb list-tables --region {{us-east-1}} --output yaml
Use auto prompt to help with a command:
aws iam create-user --cli-auto-prompt
Get an interactive wizard for an AWS resource:
aws dynamodb wizard {{new_table}}
Generate a JSON CLI Skeleton (useful for infrastructure as code):
aws dynamodb update-table --generate-cli-skeleton
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
