# weasyprint

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/weasyprint/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bzip2
,
renice
,
sha256sum
,
wc
,
php
.
weasyprint
Render HTML to PDF or PNG.
More information:
https://weasyprint.org/
.
Render an HTML file to PDF:
weasyprint {{path/to/input.html}} {{path/to/output}}.pdf
Render an HTML file to PNG, including an additional user stylesheet:
weasyprint {{path/to/input.html}} {{path/to/output}}.png --stylesheet {{path/to/stylesheet.css}}
Output additional debugging information when rendering:
weasyprint {{path/to/input.html}} {{path/to/output}}.pdf --verbose
Specify a custom resolution when outputting to PNG:
weasyprint {{path/to/input.html}} {{path/to/output}}.png --resolution {{300}}
Specify a base URL for relative URLs in the input HTML file:
weasyprint {{path/to/input.html}} {{path/to/output}}.png --base-url {{url_or_filename}}
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
