# vboxmanage

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/vboxmanage/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
topgrade
,
httprobe
,
gcal
,
cordova
.
VBoxManage
Command-line interface to VirtualBox.
Includes all the functionality of the GUI and more.
More information:
https://www.virtualbox.org/manual/ch08.html#vboxmanage-intro
.
List all VirtualBox virtual machines:
VBoxManage list vms
Show information about a particular virtual machine:
VBoxManage showvminfo {{name|uuid}}
Start a virtual machine:
VBoxManage startvm {{name|uuid}}
Start a virtual machine in headless mode:
VBoxManage startvm {{name|uuid}} --type headless
Shutdown the virtual machine and save its current state:
VBoxManage controlvm {{name|uuid}} savestate
Shutdown down the virtual machine without saving its state:
VBoxManage controlvm {{name|uuid}} poweroff
Update VBox extension packs:
VBoxManage extpack install --replace {{VboxExtensionPackFileName}}
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
