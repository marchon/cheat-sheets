# jest

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jest/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git show
,
llvm cat
,
tldrl
,
ivpn
.
jest
A zero-configuration JavaScript testing platform.
More information:
https://jestjs.io
.
Run all available tests:
jest
Run the test suites from the given files:
jest {{path/to/file1}} {{path/to/file2}}
Run the test suites from files within the current and subdirectories, whose paths match the given regular expression:
jest {{regular_expression1}} {{regular_expression2}}
Run the tests whose names match the given regular expression:
jest --testNamePattern {{regular_expression}}
Run test suites related to a given source file:
jest --findRelatedTests {{path/to/source_file.js}}
Run test suites related to all uncommitted files:
jest --onlyChanged
Watch files for changes and automatically re-run related tests:
jest --watch
Show help:
jest --help
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
