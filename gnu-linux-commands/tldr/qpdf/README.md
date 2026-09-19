# qpdf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/qpdf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
elvish
,
transmission create
.
qpdf
Versatile PDF transformation software.
More information:
https://github.com/qpdf/qpdf
.
Extract pages 1-3, 5 and 6-10 from a PDF file and save them as another one:
qpdf --empty --pages {{input.pdf}} {{1-3,5,6-10}} -- {{output.pdf}}
Merge (concatenate) all the pages of a list of PDF files and save the result as a new PDF:
qpdf --empty --pages {{file1.pdf}} {{file2.pdf}} {{file3.pdf}} -- {{output.pdf}}
Merge (concatenate) given pages from a list of PDF files and save the result as a new PDF:
qpdf --empty --pages {{file1.pdf}} {{1,6-8}} {{file2.pdf}} {{3,4,5}} -- {{output.pdf}}
Write each group of n pages to a separate output file with a given filename pattern:
qpdf --split-pages=n {{input.pdf}} {{out_%d.pdf}}
Rotate certain pages of a PDF with a given angle:
qpdf --rotate={{90:2,4,6}} --rotate={{180:7-8}} {{input.pdf}} {{output.pdf}}
Remove the password from a password-protected file:
qpdf --password={{password}} --decrypt {{input.pdf}} {{output.pdf}}
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
