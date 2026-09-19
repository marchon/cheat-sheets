# nl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
chsh
,
ebook convert
,
testssl
.
nl
A utility for numbering lines, either from a file, or from standard input.
More information:
https://www.gnu.org/software/coreutils/nl
.
Number non-blank lines in a file:
nl {{file}}
Read from standard output:
cat {{file}} | nl {{options}} -
Number only the lines with printable text:
nl -t {{file}}
Number all lines including blank lines:
nl -b a {{file}}
Number only the body lines that match a basic regular expression (BRE) pattern:
nl -b p'FooBar[0-9]' {{file}}
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
