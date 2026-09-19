# watch

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/watch/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git annex
,
singularity
,
bitcoin cli
.
watch
Execute a program periodically, showing output fullscreen.
More information:
https://manned.org/watch
.
Repeatedly run a command and show the result:
watch {{command}}
Re-run a command every 60 seconds:
watch -n {{60}} {{command}}
Monitor the contents of a directory, highlighting differences as they appear:
watch -d {{ls -l}}
Repeatedly run a pipeline and show the result:
watch '{{command_1}} | {{command_2}} | {{command_3}}'
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
