# ctest

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ctest/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gnomon
,
btm
,
ncmpcpp
,
phpstorm
.
ctest
CMake test driver program.
More information:
https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest
.
Run all tests defined in the CMake project, executing 4 jobs at a time in parallel:
ctest -j{{4}} --output-on-failure
Show a list of available tests:
ctest -N
Run a single test based on its name, or filter on a regular expression:
ctest --output-on-failure -R '^{{test_name}}$'
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
