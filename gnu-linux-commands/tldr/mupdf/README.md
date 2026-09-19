# mupdf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mupdf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
http server upload
,
encfs
,
pio init
.
mupdf
MuPDF is a lightweight PDF, XPS, and E-book viewer.
More information:
https://www.mupdf.com
.
Open a PDF on the first page:
mupdf {{filename}}
Open a PDF on page 3:
mupdf {{filename}} {{3}}
Open a password secured PDF:
mupdf -p {{password}} {{filename}}
Open a PDF with an initial zoom level, specified as DPI, of 72:
mupdf -r {{72}} {{filename}}
Open a PDF with inverted color:
mupdf -I {{filename}}
Open a PDF tinted red #FF0000 (hexadecimal color syntax RRGGBB):
mupdf -C {{FF0000}}
Open a PDF without anti-aliasing (0 = off, 8 = best):
mupdf -A {{0}}
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
