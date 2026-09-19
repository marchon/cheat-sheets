# jp2a

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jp2a/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
csh
,
dvc freeze
,
git abort
,
help2man
.
jp2a
Convert JPEG images to ASCII.
More information:
https://csl.name/jp2a/
.
Read JPEG image from a file and print in ASCII:
jp2a {{path/to/image.jpeg}}
Read JPEG image from a URL and print in ASCII:
jp2a {{www.example.com/image.jpeg}}
Colorize the ASCII output:
jp2a --colors {{path/to/image.jpeg}}
Specify characters to be used for the ASCII output:
jp2a --chars='{{..-ooxx@@}}' {{path/to/image.jpeg}}
Write the ASCII output into a file:
jp2a --output={{path/to/output_file.txt}} {{path/to/image.jpeg}}
Write the ASCII output in HTML file format, suitable for viewing in web browsers:
jp2a --html --output={{path/to/output_file.html}} {{path/to/image.jpeg}}
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
