# tokei

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tokei/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tree
,
git update index
,
pdfunite
.
tokei
A program that prints out statistics about code.
More information:
https://github.com/XAMPPRocky/tokei
.
Get a report on the code in a directory and all subdirectories:
tokei {{path/to/directory}}
Get a report for a directory excluding
.min.js
files:
tokei {{path/to/directory}} -e {{*.min.js}}
Print out statistics for individual files in a directory:
tokei {{path/to/directory}} --files
Get a report for all files of type Rust and Markdown:
tokei {{path/to/directory}} -t={{Rust}},{{Markdown}}
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
