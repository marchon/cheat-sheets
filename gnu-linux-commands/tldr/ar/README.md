# ar

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ar/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
infection
,
git commit
,
vzdump
.
ar
Create, modify, and extract from archives (
.a
,
.so
,
.o
).
More information:
https://manned.org/ar
.
Extract all members from an archive:
ar -x {{path/to/file.a}}
List the members of an archive:
ar -t {{path/to/file.a}}
Replace or add files to an archive:
ar -r {{path/to/file.a}} {{path/to/file1.o}} {{path/to/file2.o}}
Insert an object file index (equivalent to using
ranlib
):
ar -s {{path/to/file.a}}
Create an archive with files and an accompanying object file index:
ar -rs {{path/to/file.a}} {{path/to/file1.o}} {{path/to/file2.o}}
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
