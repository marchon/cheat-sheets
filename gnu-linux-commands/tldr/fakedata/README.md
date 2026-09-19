# fakedata

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fakedata/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
docker system
,
git send email
.
fakedata
Generate fake data using a large variety of generators.
More information:
https://github.com/lucapette/fakedata
.
List all valid generators:
fakedata --generators
Generate data using one or more generators:
fakedata {{generator1}} {{generator2}}
Generate data with a specific output format:
fakedata --format {{csv|tab|sql}} {{generator}}
Generate a given number of data items (defaults to 10):
fakedata --limit {{n}} {{generator}}
Generate data using a custom output template (the first letter of generator names must be capitalized):
echo "{{\{\{Generator\}\}}}" | fakedata
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
