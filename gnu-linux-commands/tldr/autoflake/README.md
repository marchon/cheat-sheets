# autoflake

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/autoflake/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
clang
,
brew cask
,
firefox
,
cdk
.
autoflake
A tool to remove unused imports and variables from Python code.
More information:
https://github.com/myint/autoflake
.
Remove unused variables from a single file and display the diff:
autoflake --remove-unused-variables {{file.py}}
Remove unused imports from multiple files and display the diffs:
autoflake --remove-all-unused-imports {{file1.py}} {{file2.py}} {{file3.py}}
Remove unused variables from a file, overwriting the file:
autoflake --remove-unused-variables --in-place {{file.py}}
Remove unused variables recursively from all files in a directory, overwriting each file:
autoflake --remove-unused-variables --in-place --recursive {{path/to/directory}}
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
