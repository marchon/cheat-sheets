# astyle

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/astyle/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
csvpy
,
lambo
,
nth
,
buzzphrase
,
clang format
.
astyle
Source code indenter, formatter, and beautifier for the C, C++, C# and Java programming languages.
Upon running, a copy of the original file is created with an ".orig" appended to the original file name.
More information:
http://astyle.sourceforge.net/
.
Apply the default style of 4 spaces per indent and no formatting changes:
astyle {{source_file}}
Apply the Java style with attached braces:
astyle --style=java {{path/to/file}}
Apply the allman style with broken braces:
astyle --style=allman {{path/to/file}}
Apply a custom indent using spaces. Choose between 2 and 20 spaces:
astyle --indent=spaces={{number_of_spaces}} {{path/to/file}}
Apply a custom indent using tabs. Choose between 2 and 20 tabs:
astyle --indent=tab={{number_of_tabs}} {{path/to/file}}
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
