# pdfgrep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pdfgrep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
standard
,
virt sysprep
,
gh run
.
pdfgrep
Search text in PDF files.
More information:
https://pdfgrep.org
.
Find lines that match pattern in a PDF:
pdfgrep {{pattern}} {{file.pdf}}
Include file name and page number for each matched line:
pdfgrep --with-filename --page-number {{pattern}} {{file.pdf}}
Do a case-insensitive search for lines that begin with "foo" and return the first 3 matches:
pdfgrep --max-count {{3}} --ignore-case {{'^foo'}} {{file.pdf}}
Find pattern in files with a
.pdf
extension in the current directory recursively:
pdfgrep --recursive {{pattern}}
Find pattern on files that match a specific glob in the current directory recursively:
pdfgrep --recursive --include {{'*book.pdf'}} {{pattern}}
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
