# diff-pdf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/diff-pdf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pueue restart
,
xev
,
git ignore io
.
diff-pdf
Tool for comparing two PDFs.
More information:
https://github.com/vslavik/diff-pdf
.
Compare PDFs, indicating changes using return codes (
0
= no difference,
1
= PDFs differ):
diff-pdf {{path/to/a.pdf}} {{path/to/b.pdf}}
Compare PDFs, outputting a PDF with visually highlighted differences:
diff-pdf --output-diff={{path/to/diff.pdf}} {{path/to/a.pdf}} {{path/to/b.pdf}}
Compare PDFs, viewing differences in a simple GUI:
diff-pdf --view {{path/to/a.pdf}} {{path/to/b.pdf}}
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
