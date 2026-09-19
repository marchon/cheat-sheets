# llvm-as

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/llvm-as/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fdp
,
bzgrep
,
keepassxc cli
,
pueue group
.
llvm-as
LLVM Intermediate Representation (
.ll
) to Bitcode (
.bc
) assembler.
More information:
https://llvm.org/docs/CommandGuide/llvm-as.html
.
Assemble an IR file:
llvm-as -o {{path/to/out.bc}} {{path/to/source.ll}}
Assemble an IR file and include a module hash in the produced Bitcode file:
llvm-as --module-hash -o {{path/to/out.bc}} {{path/to/source.ll}}
Read an IR file from
stdin
and assemble it:
cat {{path/to/source.ll}} | llvm-as -o {{path/to/out.bc}}
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
