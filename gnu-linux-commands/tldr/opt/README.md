# opt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/opt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virsh list
,
go clean
,
gdal2tiles.py
.
opt
A tool that takes LLVM source files and runs specified optimizations and/or analysis on them.
More information:
https://llvm.org/docs/CommandGuide/opt.html
.
Run an optimization or analysis on a bitcode file:
opt -{{passname}} {{path/to/file.bc}} -S -o {{file_opt.bc}}
Output the Control Flow Graph of a function to a
.dot
file:
opt {{-dot-cfg}} -S {{path/to/file.bc}} -disable-output
Optimize the program at level 2 and output the result to another file:
opt -O2 {{path/to/file.bc}} -S -o {{path/to/output_file.bc}}
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
