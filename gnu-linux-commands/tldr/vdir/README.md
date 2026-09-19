# vdir

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/vdir/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
boot
,
geth
,
wrangler
,
daps
,
s
,
bash
.
vdir
List directory contents.
Drop-in replacement for
ls -l
.
More information:
https://www.gnu.org/software/coreutils/vdir
.
List files and directories in the current directory, one per line, with details:
vdir
List with sizes displayed in human-readable units (KB, MB, GB):
vdir -h
List including hidden files (starting with a dot):
vdir -a
List files and directories sorting entries by size (largest first):
vdir -S
List files and directories sorting entries by modification time (newest first):
vdir -t
List grouping directories first:
vdir --group-directories-first
Recursively list all files and directories in a specific directory:
vdir --recursive {{path/to/directory}}
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
