# git-fame

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-fame/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
more
,
conan frogarian
,
fls
,
atq
.
git fame
Pretty-print Git repository contributions.
More information:
https://github.com/casperdcl/git-fame
.
Calculate contributions for the current Git repository:
git fame
Exclude files/directories that match the specified regular expression:
git fame --excl "{{regular_expression}}"
Calculate contributions made after the specified date:
git fame --since "{{3 weeks ago|2021-05-13}}"
Display contributions in the specified format:
git fame --format {{pipe|yaml|json|csv|tsv}}
Display contributions per file extension:
git fame --bytype
Ignore whitespace changes:
git fame --ignore-whitespace
Detect inter-file line moves and copies:
git fame -C
Detect intra-file line moves and copies:
git fame -M
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
