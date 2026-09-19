# az-storage

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/az-storage/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virsh undefine
,
vdir
,
kak
,
n
,
gitlint
.
az storage
Manage Azure Cloud Storage resources.
Part of
azure-cli
.
More information:
https://docs.microsoft.com/cli/azure/storage
.
Create a storage account:
az storage account create -g {{group_name}} -n {{account_name}} -l {{location}} --sku {{account_sku}}
List all storage accounts in a resource group:
az storage account list -g {{group_name}}
List the access keys for a storage account:
az storage account keys list -g {{group_name}} -n {{account_name}}
Delete a storage account:
az storage account delete -g {{group_name}} -n {{account_name}}
Update the minimum tls version setting for a storage account:
az storage account update --min-tls-version TLS1_2 -g {{group_name}} -n {{account_name}}
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
