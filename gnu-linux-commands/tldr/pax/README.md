# pax

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pax/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dolt add
,
openssl ts
,
bundletool dump
.
pax
Archiving and copying utility.
More information:
https://manned.org/pax.1p
.
List the contents of an archive:
pax -f {{archive.tar}}
List the contents of a gzipped archive:
pax -zf {{archive.tar.gz}}
Create an archive from files:
pax -wf {{target.tar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}
Create an archive from files, using output redirection:
pax -w {{path/to/file1}} {{path/to/file2}} {{path/to/file3}} > {{target.tar}}
Extract an archive into the current directory:
pax -rf {{source.tar}}
Copy to a directory, while keeping the original metadata;
target/
must exist:
pax -rw {{path/to/file1}} {{path/to/directory1}} {{path/to/directory2}} {{target/}}
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
