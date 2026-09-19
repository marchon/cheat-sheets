# help2man

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/help2man/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
wal
,
kotlinc
,
direnv
,
matlab
,
jarsigner
.
help2man
Produce simple man pages from an executable's
--help
and
--version
output.
More information:
https://www.gnu.org/software/help2man
.
Generate a man page for an executable:
help2man {{executable}}
Specify the "name" paragraph in the man page:
help2man {{executable}} --name {{name}}
Specify the section for the man page (defaults to 1):
help2man {{executable}} --section {{section}}
Output to a file instead of stdout:
help2man {{executable}} --output {{path/to/file}}
Display detailed help:
help2man --help
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
