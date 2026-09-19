# az-network

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/az-network/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
phan
,
pueue kill
,
deluge
,
lsd
,
git subtree
.
az network
Manage Azure Network resources.
Part of
azure-cli
.
More information:
https://docs.microsoft.com/cli/azure/network
.
List network resources in a region that are used against a subscription quota:
az network list-usages
List all virtual networks in a subscription:
az network vnet list
Create a virtual network:
az network vnet create --address-prefixes {{10.0.0.0/16}} --name {{vnet}} --resource_group {{group_name}} --submet-name {{subnet}} --subnet-prefixes {{10.0.0.0/24}}
Enable accelerated networking for a network interface card:
az network nic update --accelerated-networking true --name {{nic}} --resource-group {{resource_group}}
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
