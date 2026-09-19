# tcsh

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tcsh/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hg status
,
docker run
,
gh workflow
.
tcsh
C shell with file name completion and command line editing.
See also:
csh
.
More information:
https://manned.org/tcsh
.
Start an interactive shell session:
tcsh
Start an interactive shell session without loading startup configs:
tcsh -f
Execute specific [c]ommands:
tcsh -c "{{echo 'tcsh is executed'}}"
Execute a specific script:
tcsh {{path/to/script.tcsh}}
Check a specific script for syntax errors:
tcsh -n {{path/to/script.tcsh}}
Execute specific commands from stdin:
{{echo "echo 'tcsh is executed'"}} | tcsh
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
