# column

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/column/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
php artisan
,
box
,
tlmgr platform
.
column
Format standard input or a file into multiple columns.
Columns are filled before rows; the default separator is a whitespace.
More information:
https://manned.org/column
.
Format the output of a command for a 30 characters wide display:
printf "header1 header2\nbar foo\n" | column --output-width {{30}}
Split columns automatically and auto-align them in a tabular format:
printf "header1 header2\nbar foo\n" | column --table
Specify the column delimiter character for the
--table
option (e.g. "," for CSV) (defaults to whitespace):
printf "header1,header2\nbar,foo\n" | column --table --separator {{,}}
Fill rows before filling columns:
printf "header1\nbar\nfoobar\n" | column --output-width {{30}} --fillrows
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
