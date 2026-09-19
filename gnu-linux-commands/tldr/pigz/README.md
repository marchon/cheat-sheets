# pigz

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pigz/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kosmorro
,
pyenv
,
pueue parallel
.
pigz
Multithreaded zlib compression utility.
More information:
https://github.com/madler/pigz
.
Compress a file with default options:
pigz {{filename}}
Compress a file using the best compression method:
pigz -9 {{filename}}
Compress a file using no compression and 4 processors:
pigz -0 -p{{4}} {{filename}}
Compress a directory using tar:
tar cf - {{path/to/directory}} | pigz > {{filename}}.tar.gz
Decompress a file:
pigz -d {{archive.gz}}
List the contents of an archive:
pigz -l {{archive.tar.gz}}
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
