# csvformat

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/csvformat/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
whois
,
sqlmap
,
josm
,
timidity
,
git grep
.
csvformat
Convert a CSV file to a custom output format.
Included in csvkit.
More information:
https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html
.
Convert to a tab-delimited file (TSV):
csvformat -T {{data.csv}}
Convert delimiters to a custom character:
csvformat -D "{{custom_character}}" {{data.csv}}
Convert line endings to carriage return (^M) + line feed:
csvformat -M "{{\r\n}}" {{data.csv}}
Minimize use of quote characters:
csvformat -U 0 {{data.csv}}
Maximize use of quote characters:
csvformat -U 1 {{data.csv}}
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
