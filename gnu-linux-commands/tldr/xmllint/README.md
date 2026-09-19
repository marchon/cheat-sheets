# xmllint

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xmllint/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
safe
,
mkvmerge
,
view
,
go bug
,
rg
.
xmllint
XML parser and linter that supports XPath, a syntax for navigating XML trees.
More information:
https://manned.org/xmllint
.
Return all nodes (tags) named "foo":
xmllint --xpath "//{{foo}}" {{source_file.xml}}
Return the contents of the first node named "foo" as a string:
xmllint --xpath "string(//{{foo}})" {{source_file.xml}}
Return the href attribute of the second anchor element in an HTML file:
xmllint --html --xpath "string(//a[2]/@href)" webpage.xhtml
Return human-readable (indented) XML from file:
xmllint --format {{source_file.xml}}
Check that an XML file meets the requirements of its DOCTYPE declaration:
xmllint --valid {{source_file.xml}}
Validate XML against DTD schema hosted online:
xmllint --dtdvalid {{URL}} {{source_file.xml}}
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
