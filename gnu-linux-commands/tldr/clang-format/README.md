# clang-format

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/clang-format/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
unar
,
sd
,
mr
,
makensis
,
pixiecore
.
clang-format
Tool to auto-format C/C++/Java/JavaScript/Objective-C/Protobuf/C# code.
More information:
https://clang.llvm.org/docs/ClangFormat.html
.
Format a file and print the result to stdout:
clang-format {{path/to/file}}
Format a file in-place:
clang-format -i {{path/to/file}}
Format a file using a predefined coding style:
clang-format --style={{LLVM|Google|Chromium|Mozilla|WebKit}} {{path/to/file}}
Format a file using the
.clang-format
file in one of the parent directories of the source file:
clang-format --style=file {{path/to/file}}
Generate a custom
.clang-format
file:
clang-format --style={{LLVM|Google|Chromium|Mozilla|WebKit}} --dump-config > {{.clang-format}}
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
