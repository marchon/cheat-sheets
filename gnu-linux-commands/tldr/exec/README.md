# exec

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/exec/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
keepassxc cli
,
pueue stash
.
exec
Replace the current process with another process.
More information:
https://linuxcommand.org/lc3_man_pages/exech.html
.
Replace with the specified command using the current environment variables:
exec {{command -with -flags}}
Replace with the specified command, clearing environment variables:
exec -c {{command -with -flags}}
Replace with the specified command and login using the default shell:
exec -l {{command -with -flags}}
Replace with the specified command and change the process name:
exec -a {{process_name}} {{command -with -flags}}
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
