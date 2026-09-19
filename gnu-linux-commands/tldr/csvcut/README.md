# csvcut

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/csvcut/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git local commits
,
go test
.
csvcut
Filter and truncate CSV files. Like Unix's
cut
command, but for tabular data.
Included in csvkit.
More information:
https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html
.
Print indices and names of all columns:
csvcut -n {{data.csv}}
Extract the first and third columns:
csvcut -c {{1,3}} {{data.csv}}
Extract all columns **except** the fourth one:
csvcut -C {{4}} {{data.csv}}
Extract the columns named "id" and "first name" (in that order):
csvcut -c {{id,"first name"}} {{data.csv}}
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
