# xmlto

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xmlto/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mp4box
,
git tag
,
tmux
,
ionic
,
mixxx
.
xmlto
Apply an XSL stylesheet to an XML document.
More information:
https://pagure.io/xmlto
.
Convert a DocBook XML document to PDF format:
xmlto {{pdf}} {{document.xml}}
Convert a DocBook XML document to HTML format and store the resulting files in a separate directory:
xmlto -o {{path/to/html_files}} {{html}} {{document.xml}}
Convert a DocBook XML document to a single HTML file:
xmlto {{html-nochunks}} {{document.xml}}
Specify a stylesheet to use while converting a DocBook XML document:
xmlto -x {{stylesheet.xsl}} {{output_format}} {{document.xml}}
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
