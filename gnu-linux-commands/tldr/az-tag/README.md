# az-tag

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/az-tag/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
glab mr create
,
bg
,
redis cli
.
az tag
Manage tags on a resource.
Part of
azure-cli
.
More information:
https://docs.microsoft.com/cli/azure/tag
.
Create a tag value:
az tag add-value --name {{tag_name}} --value {{tag_value}}
Create a tag in the subscription:
az tag create --name {{tag_name}}
Delete a tag from the subscription:
az tag delete --name {{tag_name}}
List all tags on a subscription:
az tag list --resource-id /subscriptions/{{subscription_id}}
Delete a tag value for a specific tag name:
az tag remove-value --name {{tag_name}} --value {{tag_value}}
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
