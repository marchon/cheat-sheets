# xml-transform

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xml-transform/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gdrive
,
tmuxinator
,
shift
,
git root
.
xml transform
Transform XML documents using XSLT.
More information:
http://xmlstar.sourceforge.net/docs.php
.
Transform an XML document using an XSL stylesheet, passing one XPATH parameter and one literal string parameter:
xml transform {{path/to/stylesheet.xsl}} -p "{{Count='count(/xml/table/rec)'}}" -s {{Text="Count="}} {{path/to/input.xml|URI}}
Display help for the
transform
subcommand:
xml transform --help
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
