# sdiff

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sdiff/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
last
,
supervisord
,
dotnet restore
.
sdiff
Compare the differences between and optionally merge 2 files.
More information:
https://manned.org/sdiff
.
Compare 2 files:
sdiff {{path/to/file1}} {{path/to/file2}}
Compare 2 files, ignoring all tabs and whitespace:
sdiff -W {{path/to/file1}} {{path/to/file2}}
Compare 2 files, ignoring whitespace at the end of lines:
sdiff -Z {{path/to/file1}} {{path/to/file2}}
Compare 2 files in a case-insensitive manner:
sdiff -i {{path/to/file1}} {{path/to/file2}}
Compare and then merge, writing the output to a new file:
sdiff -o {{path/to/merged_file}} {{path/to/file1}} {{path/to/file2}}
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
