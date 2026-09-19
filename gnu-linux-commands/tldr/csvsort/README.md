# csvsort

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/csvsort/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
todoist
,
finger
,
nf core
,
xonsh
.
csvsort
Sorts CSV files.
Included in csvkit.
More information:
https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html
.
Sort a CSV file by column 9:
csvsort -c {{9}} {{data.csv}}
Sort a CSV file by the "name" column in descending order:
csvsort -r -c {{name}} {{data.csv}}
Sort a CSV file by column 2, then by column 4:
csvsort -c {{2,4}} {{data.csv}}
Sort a CSV file without inferring data types:
csvsort --no-inference -c {{columns}} {{data.csv}}
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
