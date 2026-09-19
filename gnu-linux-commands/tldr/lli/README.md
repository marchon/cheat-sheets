# lli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/lli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
rev
,
git range diff
,
pass
,
gcalcli
.
lli
Directly execute programs from LLVM bitcode.
More information:
https://www.llvm.org/docs/CommandGuide/lli.html
.
Execute a bitcode or IR file:
lli {{path/to/file.ll}}
Execute with command line arguments:
lli {{path/to/file.ll}} {{argument1 argument2 ...}}
Enable all optimizations:
lli -O3 {{path/to/file.ll}}
Load a dynamic library before linking:
lli --dlopen={{path/to/library.dll}} {{path/to/file.ll}}
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
