# pdftk

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pdftk/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
2to3
,
sync
,
git abort
,
stdbuf
,
mullvad
.
pdftk
PDF toolkit.
More information:
https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit
.
Extract pages 1-3, 5 and 6-10 from a PDF file and save them as another one:
pdftk {{input.pdf}} cat {{1-3 5 6-10}} output {{output.pdf}}
Merge (concatenate) a list of PDF files and save the result as another one:
pdftk {{file1.pdf file2.pdf ...}} cat output {{output.pdf}}
Split each page of a PDF file into a separate file, with a given filename output pattern:
pdftk {{input.pdf}} burst output {{out_%d.pdf}}
Rotate all pages by 180 degrees clockwise:
pdftk {{input.pdf}} cat {{1-endsouth}} output {{output.pdf}}
Rotate third page by 90 degrees clockwise and leave others unchanged:
pdftk {{input.pdf}} cat {{1-2 3east 4-end}} output {{output.pdf}}
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
