# xgettext

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xgettext/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
apktool
,
kind
,
middleman
,
vifm
.
xgettext
Extract gettext strings from code files.
More information:
https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html
.
Scan file and output strings to
messages.po
:
xgettext {{path/to/input_file}}
Use a different output filename:
xgettext --output {{path/to/output_file}} {{path/to/input_file}}
Append new strings to an existing file:
xgettext --join-existing --output {{path/to/output_file}} {{path/to/input_file}}
Don't add a header containing metadata to the output file:
xgettext --omit-header {{path/to/input_file}}
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
