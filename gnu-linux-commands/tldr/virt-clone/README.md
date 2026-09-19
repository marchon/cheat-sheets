# virt-clone

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virt-clone/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ifconfig
,
mosquitto_sub
,
base64
.
virt-clone
Clone a libvirt virtual machine.
More information:
https://manned.org/virt-clone
.
Clone a virtual machine and automatically generate a new name, storage path, and MAC address:
virt-clone --original {{vm_name}} --auto-clone
Clone a virtual machine and specify the new name, storage path, and MAC address:
virt-clone --original {{vm_name}} --name {{new_vm_name}} --file {{path/to/new_storage}} --mac {{ff:ff:ff:ff:ff:ff|RANDOM}}
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
