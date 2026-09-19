# csslint

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/csslint/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mesg
,
view
,
vcsh
,
mh_copyright
.
csslint
A linter for CSS code.
More information:
https://github.com/CSSLint/csslint/wiki/Command-line-interface
.
Lint a single CSS file:
csslint {{file.css}}
Lint multiple CSS files:
csslint {{file1.css}} {{file2.css}} {{file3.css}}
List all possible style rules:
csslint --list-rules
Specify certain rules as errors (which result in a non-zero exit code):
csslint --errors={{errors,universal-selector,imports}} {{file.css}}
Specify certain rules as warnings:
csslint --warnings={{box-sizing,selector-max,floats}} {{file.css}}
Specify certain rules to ignore:
csslint --ignore={{ids,rules-count,shorthand}} {{file.css}}
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
