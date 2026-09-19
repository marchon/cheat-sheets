# mlr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mlr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virt install
,
csslint
,
pnpm
,
crictl
.
mlr
Miller is like
awk
,
sed
,
cut
,
join
, and
sort
for name-indexed data such as CSV, TSV, and tabular JSON.
More information:
https://johnkerl.org/miller/doc
.
Pretty-print a CSV file in a tabular format:
mlr --icsv --opprint cat {{example.csv}}
Receive JSON data and pretty print the output:
echo '{"hello":"world"}' | mlr --ijson --opprint cat
Sort alphabetically on a field:
mlr --icsv --opprint sort -f {{field}} {{example.csv}}
Sort in descending numerical order on a field:
mlr --icsv --opprint sort -nr {{field}} {{example.csv}}
Convert CSV to JSON, performing calculations and display those calculations:
mlr --icsv --ojson put '${{newField1}} = ${{oldFieldA}}/${{oldFieldB}}' {{example.csv}}
Receive JSON and format the output as vertical JSON:
echo '{"hello":"world", "foo":"bar"}' | mlr --ijson --ojson --jvstack cat
Filter lines of a compressed CSV file treating numbers as strings:
mlr --prepipe 'gunzip' --csv filter -S '${{fieldName}} =~ "{{regular_expression}}"' {{example.csv.gz}}
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
