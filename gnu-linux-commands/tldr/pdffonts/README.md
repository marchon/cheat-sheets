# pdffonts

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pdffonts/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
llvm g++
,
ab
,
fdp
,
odps tunnel
.
pdffonts
Portable Document Format (PDF) file fonts information viewer.
More information:
https://www.xpdfreader.com/pdffonts-man.html
.
Print PDF file fonts information:
pdffonts {{path/to/file.pdf}}
Specify user password for PDF file to bypass security restrictions:
pdffonts -upw {{password}} {{path/to/file.pdf}}
Specify owner password for PDF file to bypass security restrictions:
pdffonts -opw {{password}} {{path/to/file.pdf}}
Print additional information on location of the font that will be used when the PDF file is rasterized:
pdffonts -loc {{path/to/file.pdf}}
Print additional information on location of the font that will be used when the PDF file is converted to PostScript:
pdffonts -locPS {{path/to/file.pdf}}
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
