# func

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/func/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xkcdpass
,
trans
,
ag
,
openvpn
,
zipinfo
.
func
Azure Functions Core Tools: Develop and test Azure Functions locally.
Local functions can connect to live Azure services, and can deploy a function app to an Azure subscription.
More information:
https://docs.microsoft.com/azure/azure-functions/functions-run-local
.
Create a new functions project:
func init {{project}}
Create a new function:
func new
Run functions locally:
func start
Publish your code to a function app in Azure:
func azure functionapp publish {{function}}
Download all settings from an existing function app:
func azure functionapp fetch-app-settings {{function}}
Get the connection string for a specific storage account:
func azure storage fetch-connection-string {{storage_account}}
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
