# mv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bc
,
is up
,
progpilot
,
circo
,
sqlite3
.
mv
Move or rename files and directories.
More information:
https://www.gnu.org/software/coreutils/mv
.
Move a file to an arbitrary location:
mv {{source}} {{target}}
Move files into another directory, keeping the filenames:
mv {{source1}} {{source2}} {{source3}} {{target_directory}}
Do not prompt for confirmation before overwriting existing files:
mv -f {{source}} {{target}}
Prompt for confirmation before overwriting existing files, regardless of file permissions:
mv -i {{source}} {{target}}
Do not overwrite existing files at the target:
mv -n {{source}} {{target}}
Move files in verbose mode, showing files after they are moved:
mv -v {{source}} {{target}}
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
