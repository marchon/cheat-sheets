# exrex

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/exrex/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pipenv
,
adscript
,
grpcurl
,
pngcheck
.
exrex
Generate all/random matching strings for a regular expression.
It can also simplify regular expressions.
More information:
https://github.com/asciimoo/exrex
.
Generate all possible strings that match a regular expression:
exrex '{{regular_expression}}'
Generate a random string that matches a regular expression:
exrex --random '{{regular_expression}}'
Generate at most 100 strings that match a regular expression:
exrex --max-number {{100}} '{{regular_expression}}'
Generate all possible strings that match a regular expression, joined by a custom delimiter string:
exrex --delimiter "{{, }}" '{{regular_expression}}'
Print count of all possible strings that match a regular expression:
exrex --count '{{regular_expression}}'
Simplify a regular expression:
exrex --simplify '{{ab|ac}}'
Print eyes:
exrex '{{[oO0](_)[oO0]}}'
Print a boat:
exrex '{{( {20}(\| *\\|-{22}|\|)|\.={50}| ( ){0,5}\\\.| {12}~{39})}}'
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
