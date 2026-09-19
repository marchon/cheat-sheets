# img2pdf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/img2pdf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git local commits
,
git ls files
.
img2pdf
Command-line lossless converter of raster images to PDF.
More information:
https://gitlab.mister-muffin.de/josch/img2pdf
.
Convert multiple images to a single PDF, each image being on its own page:
img2pdf {{path/to/image1.jpg}} {{path/to/image2.jpg}} --output {{path/to/file.pdf}}
Convert only the first frame of a multi-frame image to PDF:
img2pdf {{path/to/file.gif}} --first-frame-only --output {{path/to/file.pdf}}
Auto orient the image, use a page size of A4 in landscape mode, and set a border of 2cm horizontally and 5.1cm vertically:
img2pdf {{path/to/file.jpg}} --auto-orient --pagesize {{A4^T}} --border {{2cm}}:{{5.1cm}} --output {{path/to/file.pdf}}
Shrink only larger images to a 10cm by 15cm rectangle inside a 30x20cm page:
img2pdf {{path/to/file.tiff}} --pagesize {{30cm}}x{{20cm}} --imgsize {{10cm}}x{{15cm}} --fit {{shrink}} --output {{path/to/file.pdf}}
Convert an image to PDF, and specify metadata for the resulting file:
img2pdf {{path/to/file.png}} --title {{title}} --author {{author}} --creationdate {{1970-01-31}} --keywords {{keyword1 keyword2}} --subject {{subject}} --output {{path/to/file.pdf}}
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
