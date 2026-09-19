# in2csv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/in2csv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dvc freeze
,
git mr
,
qrencode
.
in2csv
Converts various tabular data formats into CSV.
Included in csvkit.
More information:
https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html
.
Convert an XLS file to CSV:
in2csv {{data.xls}}
Convert a DBF file to a CSV file:
in2csv {{data.dbf}} > {{data.csv}}
Convert a specific sheet from an XLSX file to CSV:
in2csv --sheet={{sheet_name}} {{data.xlsx}}
Pipe a JSON file to in2csv:
cat {{data.json}} | in2csv -f json > {{data.csv}}
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
