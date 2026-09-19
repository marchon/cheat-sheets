# az-appconfig

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/az-appconfig/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ant
,
git ls remote
,
direnv
,
xml validate
.
az appconfig
Manage App configurations on Azure.
Part of
az
, the command-line client for Microsoft Azure.
More information:
https://docs.microsoft.com/cli/azure/appconfig
.
Create an App Configuration:
az appconfig create --name {{name}} --resource-group {{group_name}} --location {{location}}
Delete a specific App Configuration:
az appconfig delete --resource-group {{rg_name}} --name {{appconfig_name}}
List all App Configurations under the current subscription:
az appconfig list
List all App Configurations under a specific resource group:
az appconfig list --resource-group {{rg_name}}
Show properties of an App Configuration:
az appconfig show --name {{appconfig_name}}
Update a specific App Configuration:
az appconfig update --resource-group {{rg_name}} --name {{appconfig_name}}
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
