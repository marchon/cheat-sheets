# pdftotext

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pdftotext/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ybacklight
,
traceroute
,
tea
,
lebab
.
pdftotext
Convert PDF files to plain text format.
More information:
https://www.xpdfreader.com/pdftotext-man.html
.
Convert
filename.pdf
to plain text and print it to standard output:
pdftotext {{filename.pdf}} -
Convert
filename.pdf
to plain text and save it as
filename.txt
:
pdftotext {{filename.pdf}}
Convert
filename.pdf
to plain text and preserve the layout:
pdftotext -layout {{filename.pdf}}
Convert
input.pdf
to plain text and save it as
output.txt
:
pdftotext {{input.pdf}} {{output.txt}}
Convert pages 2, 3 and 4 of
input.pdf
to plain text and save them as
output.txt
:
pdftotext -f {{2}} -l {{4}} {{input.pdf}} {{output.txt}}
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
