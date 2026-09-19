# csvstat

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/csvstat/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tlmgr info
,
phpbu
,
pio org
,
tye
.
csvstat
Print descriptive statistics for all columns in a CSV file.
Included in csvkit.
More information:
https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html
.
Show all stats for all columns:
csvstat {{data.csv}}
Show all stats for columns 2 and 4:
csvstat -c {{2,4}} {{data.csv}}
Show sums for all columns:
csvstat --sum {{data.csv}}
Show the max value length for column 3:
csvstat -c {{3}} --len {{data.csv}}
Show the number of unique values in the "name" column:
csvstat -c {{name}} --unique {{data.csv}}
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
