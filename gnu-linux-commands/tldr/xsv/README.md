# xsv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xsv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hcloud
,
sftp
,
ogrmerge.py
,
lorem
.
xsv
A CSV command-line toolkit written in Rust.
More information:
https://github.com/BurntSushi/xsv
.
Inspect the headers of a file:
xsv headers {{path/to/file.csv}}
Count the number of entries:
xsv count {{path/to/file.csv}}
Get an overview of the shape of entries:
xsv stats {{path/to/file.csv}} | xsv table
Select a few columns:
xsv select {{column_a,column_b}} {{path/to/file.csv}}
Show 10 random entries:
xsv sample {{10}} {{path/to/file.csv}}
Join a column from one file to another:
xsv join --no-case {{column_a}} {{path/to/file/a.csv}} {{column_b}} {{path/to/file/b.csv}} | xsv table
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
