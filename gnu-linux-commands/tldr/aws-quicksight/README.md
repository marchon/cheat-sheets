# aws-quicksight

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-quicksight/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cryfs
,
gh codespace
,
go list
.
aws quicksight
CLI for AWS QuickSight.
Access QuickSight entities.
More information:
https://docs.aws.amazon.com/cli/latest/reference/quicksight/
.
List datasets:
aws quicksight list-data-sets --aws-account-id {{aws_account_id}}
List users:
aws quicksight list-users --aws-account-id {{aws_account_id}} --namespace default
List groups:
aws quicksight list-groups --aws-account-id {{aws_account_id}} --namespace default
List dashboards:
aws quicksight list-dashboards --aws-account-id {{aws_account_id}}
Display detailed information about a dataset:
aws quicksight describe-data-set --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}
Display who has access to the dataset and what kind of actions they can perform on the dataset:
aws quicksight describe-data-set-permissions --aws-account-id {{aws_account_id}} --data-set-id {{data_set_id}}
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
