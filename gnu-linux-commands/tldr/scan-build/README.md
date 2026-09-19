# scan-build

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/scan-build/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gcc
,
coffee
,
cargo doc
,
mm2gv
,
in toto record
.
scan-build
Command-line utility to run a static analyzer over a codebase as part of performing a regular build.
More information:
https://clang-analyzer.llvm.org/scan-build.html
.
Build and analyze the project in the current directory:
scan-build {{make}}
Run a command and pass all subsequent options to it:
scan-build {{command}} {{command_arguments}}
Display help:
scan-build
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
