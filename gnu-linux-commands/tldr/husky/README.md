# husky

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/husky/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
go list
,
kak
,
clifm
,
amass
,
aws
,
git missing
.
husky
Native Git hooks made easy.
More information:
https://typicode.github.io/husky
.
Install Husky in the current directory:
husky install
Install Husky into a specific directory:
husky install {{path/to/directory}}
Set a specific command as a
pre-push
hook for Git:
husky set {{.husky/pre-push}} "{{command}} {{command_arguments}}"
Add a specific command to the current
pre-commit
hook:
husky add {{.husky/pre-commit}} "{{command}} {{command_arguments}}"
Uninstall Husky hooks from the current directory:
husky uninstall
Display help:
husky
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
