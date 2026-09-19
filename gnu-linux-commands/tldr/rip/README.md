# rip

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rip/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
searchsploit
,
smartctl
,
conda create
.
rip
Remove files or directories by sending them to the graveyard, allowing for them to be recovered.
More information:
https://github.com/nivekuil/rip
.
Remove files or directories from specified locations and place them in the graveyard:
rip {{path/to/file_or_directory}} {{path/to/another/file_or_directory}}
Interactively remove files or directories, with a prompt before every removal:
rip --inspect {{path/to/file_or_directory}} {{path/to/another/file_or_directory}}
List all files and directories in the graveyard that were originally within the current directory:
rip --seance
Permanently delete every file and directory in the graveyard:
rip --decompose
Put back the files and directories which were affected by the most recent removal:
rip --unbury
Put back every file and directory that is listed by
rip --seance
:
rip --seance --unbury
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
