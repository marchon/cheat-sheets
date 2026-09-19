# plesk

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/plesk/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ansible vault
,
deemix
,
fish
,
write
.
plesk
Plesk hosting control panel CLI interface.
More information:
https://docs.plesk.com
.
Generate an auto login link for the admin user and print it:
plesk login
Show product version information:
plesk version
List all hosted domains:
plesk bin domain --list
Start watching for changes in the
panel.log
file:
plesk log {{panel.log}}
Start the interactive MySQL console:
plesk db
Open the Plesk main configuration file in the default editor:
plesk conf {{panel.ini}}
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
