# kdeconnect-cli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kdeconnect-cli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dumpcap
,
ctest
,
id
,
strip nondeterminism
.
kdeconnect-cli
KDE Connect CLI.
More information:
https://kdeconnect.kde.org
.
List all devices:
kdeconnect-cli --list-devices
List available (paired and reachable) devices:
kdeconnect-cli --list-available
Request pairing with a specific device, specifying its ID:
kdeconnect-cli --pair --device {{device_id}}
Ring a device, specifying its name:
kdeconnect-cli --ring --name {{device_name}}
Share an URL or file with a paired device, specifying its ID:
kdeconnect-cli --share {{URL|path/to/file}} --device {{device_id}}
Send an SMS with an optional attachment to a specific number:
kdeconnect-cli --name {{device_name}} --send-sms {{message}} --destination {{phone_number}} --attachment {{path/to/file}}
Unlock a specific device:
kdeconnect-cli --name {{device_name}} --unlock
Simulate a key press on a specific device:
kdeconnect-cli --name {{device_name}} --send-keys {{key}}
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
