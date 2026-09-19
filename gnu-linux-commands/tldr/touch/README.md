# touch

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/touch/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
betty
,
sqsc
,
tslint
,
openconnect
.
touch
Change a file access and modification times (atime, mtime).
More information:
https://www.gnu.org/software/coreutils/touch
.
Create a new empty file(s) or change the times for existing file(s) to current time:
touch {{path/to/file}}
Set the times on a file to a specific date and time:
touch -t {{YYYYMMDDHHMM.SS}} {{path/to/file}}
Set the time on a file to one hour in the past:
touch -d "{{-1 hour}}" {{path/to/file}}
Use the times from a file to set the times on a second file:
touch -r {{path/to/file1}} {{path/to/file2}}
Create multiple files:
touch {{path/to/file{1,2,3}.txt}}
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
