# cppclean

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cppclean/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
flow
,
makensis
,
xml transform
.
cppclean
Find unused code in C++ projects.
More information:
https://github.com/myint/cppclean
.
Run in a project's directory:
cppclean {{path/to/project}}
Run on a project where the headers are in the
inc1/
and
inc2/
directories:
cppclean {{path/to/project}} --include-path={{inc1}} --include-path={{inc2}}
Run on a specific file
main.cpp
:
cppclean {{main.cpp}}
Run on the current directory, excluding the "build" directory:
cppclean {{.}} --exclude={{build}}
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
