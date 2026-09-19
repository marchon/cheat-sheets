# idnits

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/idnits/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git cherry
,
go mod
,
snyk
,
uniq
.
idnits
Check internet-drafts for submission nits.
Looks for violations of Section 2.1 and 2.2 of the requirements listed on
https://www.ietf.org/id-info/checklist
.
More information:
https://tools.ietf.org/tools/idnits/
.
Check a file for nits:
idnits {{path/to/file.txt}}
Count nits without displaying them:
idnits --nitcount {{path/to/file.txt}}
Show extra information about offending lines:
idnits --verbose {{path/to/file.txt}}
Expect the specified year in the boilerplate instead of the current year:
idnits --year {{2021}} {{path/to/file.txt}}
Assume the document is of the specified status:
idnits --doctype {{standard|informational|experimental|bcp|ps|ds}} {{path/to/file.txt}}
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
