# llvm-bcanalyzer

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/llvm-bcanalyzer/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
eva
,
goreload
,
tb
,
androguard
,
unalias
.
llvm-bcanalyzer
LLVM Bitcode (
.bc
) analyzer.
More information:
https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html
.
Print statistics about a Bitcode file:
llvm-bcanalyzer {{path/to/file.bc}}
Print an SGML representation and statistics about a Bitcode file:
llvm-bcanalyzer -dump {{path/to/file.bc}}
Read a Bitcode file from
stdin
and analyze it:
cat {{path/to/file.bc}} | llvm-bcanalyzer
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
