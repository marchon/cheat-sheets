# llvm-config

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/llvm-config/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pio device
,
wpa_supplicant
.
llvm-config
Get various configuration information needed to compile programs which use LLVM.
Typically called from build systems, like in Makefiles or configure scripts.
More information:
https://llvm.org/docs/CommandGuide/llvm-config.html
.
Compile and link an LLVM based program:
clang++ $(llvm-config --cxxflags --ldflags --libs) --output {{path/to/output_executable}} {{path/to/source.cc}}
Print the
PREFIX
of your LLVM installation:
llvm-config --prefix
Print all targets supported by your LLVM build:
llvm-config --targets-built
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
