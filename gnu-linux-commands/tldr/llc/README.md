# llc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/llc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
scrcpy
,
pssh
,
ffmpeg
,
lighthouse
.
llc
Compiles LLVM Intermediate Representation or bitcode to target-specific assembly language.
More information:
https://www.llvm.org/docs/CommandGuide/llc.html
.
Compile a bitcode or IR file to an assembly file with the same base name:
llc {{path/to/file.ll}}
Enable all optimizations:
llc -O3 {{path/to/input.ll}}
Output assembly to a specific file:
llc --output {{path/to/output.s}}
Emit fully relocateable, position independent code:
llc -relocation-model=pic {{path/to/input.ll}}
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
