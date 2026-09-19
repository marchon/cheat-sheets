# az-login

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/az-login/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aws secretsmanager
,
mix
,
github label sync
.
az login
Log in to Azure.
Part of
az
, the command-line client for Microsoft Azure.
More information:
https://docs.microsoft.com/cli/azure/reference-index#az_login
.
Log in interactively:
az login
Log in with a service principal using a client secret:
az login --service-principal --username {{http://azure-cli-service-principal}} --passsword {{secret}} --tenant {{someone.onmicrosoft.com}}
Log in with a service principal using a client certificate:
az login --service-principal --username {{http://azure-cli-service-principal}} --password {{path/to/cert.pem}} --tenant {{someone.onmicrosoft.com}}
Log in using a VM's system assigned identity:
az login --identity
Log in using a VM's user assigned identity:
az login --identity --username /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}
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
