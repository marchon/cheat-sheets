# csvgrep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/csvgrep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
glab mr merge
,
more
,
gvpack
,
ledger
.
csvgrep
Filter CSV rows with string and pattern matching.
Included in csvkit.
More information:
https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html
.
Find rows that have a certain string in column 1:
csvgrep -c {{1}} -m {{string_to_match}} {{data.csv}}
Find rows in which columns 3 or 4 match a certain regular expression:
csvgrep -c {{3,4}} -r {{regular_expression}} {{data.csv}}
Find rows in which the "name" column does NOT include the string "John Doe":
csvgrep -i -c {{name}} -m "{{John Doe}}" {{data.csv}}
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
