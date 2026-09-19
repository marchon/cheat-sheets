# pdfseparate

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pdfseparate/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
w
,
couchdb
,
pdffonts
,
emulator
.
pdfseparate
Portable Document Format (PDF) file page extractor.
More information:
https://manpages.debian.org/unstable/poppler-utils/pdfseparate.1.en.html
.
Extract pages from PDF file and make a separate PDF file for each page:
pdfseparate {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}
Specify the first/start page for extraction:
pdfseparate -f {{3}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}
Specify the last page for extraction:
pdfseparate -l {{10}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}
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
