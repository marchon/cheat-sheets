# pgrep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pgrep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dvc init
,
meshlabserver
,
rtl_sdr
.
pgrep
Find or signal processes by name.
More information:
https://www.man7.org/linux/man-pages/man1/pkill.1.html
.
Return PIDs of any running processes with a matching command string:
pgrep {{process_name}}
Search for processes including their command-line options:
pgrep --full "{{process_name}} {{parameter}}"
Search for processes run by a specific user:
pgrep --euid root {{process_name}}
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
