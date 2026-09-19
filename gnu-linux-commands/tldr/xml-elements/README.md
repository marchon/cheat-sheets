# xml-elements

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xml-elements/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mosh
,
circo
,
singularity
,
core validate commit
.
xml elements
Extract elements and display the structure of an XML document.
More information:
http://xmlstar.sourceforge.net/docs.php
.
Extract elements from an XML document (producing XPATH expressions):
xml elements {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}
Extract elements and their attributes from an XML document:
xml elements -a {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}
Extract elements and their attributes and values from an XML document:
xml elements -v {{path/to/input.xml|URI}} > {{path/to/elements.xpath}}
Print sorted unique elements from an XML document to see its structure:
xml elements -u {{path/to/input.xml|URI}}
Print sorted unique elements from an XML document up to a depth of 3:
xml elements -d{{3}} {{path/to/input.xml|URI}}
Display help for the
elements
subcommand:
xml elements --help
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
