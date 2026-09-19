# az-lock

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/az-lock/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
slimrb
,
pssh
,
dog
,
piactl
,
expose
.
az lock
Manage Azure locks.
Part of
azure-cli
.
More information:
https://docs.microsoft.com/cli/azure/lock
.
Create a read-only subscription level lock:
az lock create --name {{lock_name}} --lock-type ReadOnly
Create a read-only resource group level lock:
az lock create --name {{lock_name}} --resource-group {{group_name}} --lock-type ReadOnly
Delete a subscription level lock:
az lock delete --name {{lock_name}}
Delete a resource group level lock:
az lock delete --name {{lock_name}} --resource-group {{group_name}}
List out all locks on the subscription level:
az lock list
Show a subscription level lock:
az lock show -n {{lock_name}}
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
