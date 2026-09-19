# llvm-dis

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/llvm-dis/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
c99
,
mixxx
,
dvc freeze
,
xml escape
.
llvm-dis
Converts LLVM bitcode files into human-readable LLVM Intermediate Representation (IR).
More information:
https://www.llvm.org/docs/CommandGuide/llvm-dis.html
.
Convert a bitcode file as LLVM IR and write the result to stdout:
llvm-dis {{path/to/input.bc}} -o -
Convert a bitcode file to an LLVM IR file with the same filename:
llvm-dis {{path/to/file.bc}}
Convert a bitcode file to LLVM IR, writing the result to the specified file:
llvm-dis {{path/to/input.bc}} -o {{path/to/output.ll}}
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
