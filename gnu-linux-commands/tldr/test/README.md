# test

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/test/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
swift
,
ssh keygen
,
llvm ar
,
roll
.
test
Check file types and compare values.
Returns 0 if the condition evaluates to true, 1 if it evaluates to false.
More information:
https://www.gnu.org/software/coreutils/test
.
Test if a given variable is equal to a given string:
test "{{$MY_VAR}}" == "{{/bin/zsh}}"
Test if a given variable is empty:
test -z "{{$GIT_BRANCH}}"
Test if a file exists:
test -f "{{path/to/file_or_directory}}"
Test if a directory does not exist:
test ! -d "{{path/to/directory}}"
If-else statement:
test {{condition}} && {{echo "true"}} || {{echo "false"}}
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
