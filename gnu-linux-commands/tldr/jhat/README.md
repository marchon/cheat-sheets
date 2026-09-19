# jhat

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jhat/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
killall
,
laravel
,
wal
,
git notes
.
jhat
Java Heap Analysis Tool.
More information:
https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html
.
Analyze a heap dump (from
jmap
), view via HTTP on port 7000:
jhat {{dump_file.bin}}
Analyze a heap dump, specifying an alternate port for the http server:
jhat -p {{port}} {{dump_file.bin}}
Analyze a dump letting
jhat
use up to 8 GB RAM (2-4x dump size recommended):
jhat -J-mx8G {{dump_file.bin}}
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
