# flake8

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/flake8/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
install tl
,
ptpython3
,
phpstan
.
flake8
Tool to check the style and quality of Python code.
More information:
https://flake8.pycqa.org/
.
Lint a file or directory recursively:
flake8 {{path/to/file_or_directory}}
Lint a file or directory recursively and show the line on which each error occurred:
flake8 --show-source {{path/to/file_or_directory}}
Lint a file or directory recursively and ignore a list of rules. (All available rules can be found at flake8rules.com):
flake8 --ignore {{rule1,rule2}} {{path/to/file_or_directory}}
Lint a file or directory recursively but exclude files matching the given globs or substrings:
flake8 --exclude {{substring1,glob2}} {{path/to/file_or_directory}}
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
