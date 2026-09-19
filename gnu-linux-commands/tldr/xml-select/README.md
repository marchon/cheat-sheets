# xml-select

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xml-select/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git undo
,
pueue shutdown
,
latex
.
xml select
Select from XML documents using XPATHs.
Tip: use
xml elements
to display the XPATHs of an XML document.
More information:
http://xmlstar.sourceforge.net/docs.php
.
Select all elements matching "XPATH1" and print the value of their sub-element "XPATH2":
xml select --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" {{path/to/input.xml|URI}}
Match  "XPATH1" and print the value of "XPATH2" as text with new-lines:
xml select --text --template --match "{{XPATH1}}" --value-of "{{XPATH2}}" --nl {{path/to/input.xml|URI}}
Count the elements of "XPATH1":
xml select --template --value-of "count({{XPATH1}})" {{path/to/input.xml|URI}}
Count all nodes in one or more XML documents:
xml select --text --template --inp-name --output " " --value-of "count(node())" --nl {{path/to/input1.xml|URI}} {{path/to/input2.xml|URI}}
Display help for the
select
subcommand:
xml select --help
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
