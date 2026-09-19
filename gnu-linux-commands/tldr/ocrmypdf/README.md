# ocrmypdf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ocrmypdf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pdfjam
,
nkf
,
cargo clippy
,
mate dictionary
.
ocrmypdf
Generate a searchable PDF or PDF/A from a scanned PDF or an image of text.
More information:
https://ocrmypdf.readthedocs.io/en/latest/cookbook.html
.
Create a new searchable PDF/A file from a scanned PDF or image file:
ocrmypdf {{path/to/input_file}} {{path/to/output.pdf}}
Replace a scanned PDF file with a searchable PDF file:
ocrmypdf {{path/to/file.pdf}} {{path/to/file.pdf}}
Skip pages of a mixed-format input PDF file that already contain text:
ocrmypdf --skip-text {{path/to/input.pdf}} {{path/to/output.pdf}}
Clean, de-skew, and rotate pages of a poor scan:
ocrmypdf --clean --deskew --rotate-pages {{path/to/input_file}} {{path/to/output.pdf}}
Set the metadata of the searchable PDF file:
ocrmypdf --title "{{title}}" --author "{{author}}" --subject "{{subject}}" --keywords "{{keyword; key phrase; ...}}" {{path/to/input_file}} {{path/to/output.pdf}}
Display help:
ocrmypdf --help
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
