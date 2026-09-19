# aws-iam

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-iam/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ex
,
chsh
,
beanstalkd
,
fls
,
zstd
,
printenv
.
aws iam
CLI for AWS IAM.
More information:
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html
.
Show
aws iam
help page (including all available iam commands):
aws iam help
List users:
aws iam list-users
List policies:
aws iam list-policies
List groups:
aws iam list-groups
Get users in a group:
aws iam get-group --group-name {{group_name}}
Describe an IAM policy:
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{policy_name}}
List access keys:
aws iam list-access-keys
List access keys for a specific user:
aws iam list-access-keys --user-name {{user_name}}
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
