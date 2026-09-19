# az-vm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/az-vm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
trivy
,
pdffonts
,
banner
,
gdalbuildvrt
.
az vm
Manage virtual machines in Azure.
Part of
az
, the command-line client for Microsoft Azure.
More information:
https://docs.microsoft.com/cli/azure/vm
.
List details of available Virtual Machines:
az vm list
Create an
UbuntuServer 18.04 LTS
Virtual Machine and generate ssh keys:
az vm create --resource-group {{rg}} --name {{vm_name}} --image {{Canonical:UbuntuServer:18.04-LTS:latest}} --admin-user {{azureuser}} --generate-ssh-keys
Stop a Virtual Machine:
az vm stop --resource-group {{rg}} --name {{vm_name}}
Deallocate a Virtual Machine:
az vm deallocate --resource-group {{rg}} --name {{vm_name}}
Start a Virtual Machine:
az vm start --resource-group {{rg}} --name {{vm_name}}
Restart a Virtual Machine:
az vm restart --resource-group {{rg}} --name {{vm_name}}
List VM images available in the Azure Marketplace:
az vm image list
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
