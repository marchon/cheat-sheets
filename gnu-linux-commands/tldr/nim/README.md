# nim

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nim/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virsh pool start
,
git fsck
.
nim
The Nim compiler.
Processes, compiles and links Nim language source files.
More information:
https://nim-lang.org
.
Compile a source file:
nim compile {{file.nim}}
Compile and run a source file:
nim compile -r {{file.nim}}
Compile a source file with release optimizations enabled:
nim compile -d:release {{file.nim}}
Build a release binary optimized for low file size:
nim compile -d:release --opt:size {{file.nim}}
Generate HTML documentation for a module (output will be placed in the current directory):
nim doc {{file.nim}}
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
