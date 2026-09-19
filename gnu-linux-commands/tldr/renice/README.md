# renice

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/renice/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fossa
,
hadolint
,
xmlto
,
source
.
renice
Alters the scheduling priority/nicenesses of one or more running processes.
Niceness values range from -20 (most favorable to the process) to 19 (least favorable to the process).
More information:
https://manned.org/renice
.
Change priority of a running process:
renice -n {{niceness_value}} -p {{pid}}
Change priority of all processes owned by a user:
renice -n {{niceness_value}} -u {{user}}
Change priority of all processes that belong to a process group:
renice -n {{niceness_value}} --pgrp {{process_group}}
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
