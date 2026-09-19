# az-storage-blob

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/az-storage-blob/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aws s3api
,
progress
,
cdk
,
ansible vault
.
az storage blob
Manage blob storage containers and objects in Azure.
Part of
azure-cli
.
More information:
https://docs.microsoft.com/cli/azure/storage/blob
.
Download a blob to a file path:
az storage blob download --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} -f {{path/to/local_file}}
Download blobs from a blob container recursively:
az storage blob download-batch --account-name {{storage_account_name}} --account-key {{storage_account_key}} -s {{container_name}} -d {{path/to/remote}} --pattern {{filename_regex}} --destination {{path/to/destination}}
Upload a local file to blob storage:
az storage blob upload --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} -f {{path/to/local_file}}
Delete a blob object:
az storage blob delete --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}}
Generate a shared access signature for a blob:
az storage blob generate-sas --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} --permissions {{permission_set}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only
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
