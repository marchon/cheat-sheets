# az-storage-entity

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/az-storage-entity/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kate
,
glab mr
,
multitail
,
aws
,
isisdl
.
az storage entity
Manage Azure Table storage entities.
Part of
azure-cli
.
More information:
https://docs.microsoft.com/cli/azure/storage/entity
.
Insert an entity into a table:
az storage entity insert --entity {{space_separated_key_value_pairs}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}
Delete an existing entity from a table:
az storage entity delete --partition-key {{partition_key}} --row-key {{row_key}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}
Update an existing entity by merging its properties:
az storage entity merge --entity {{space_separated_key_value_pairs}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}
List entities which satisfy a query:
az storage entity query --filter {{query_filter}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}
Get an entity from the specified table:
az storage entity show --partition-key {{partition_key}} --row-key {{row_key}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}
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
