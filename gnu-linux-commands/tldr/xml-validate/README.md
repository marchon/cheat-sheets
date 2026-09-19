# xml-validate

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xml-validate/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hostid
,
espeak
,
fastlane
,
hg branch
.
xml validate
Validate XML documents.
More information:
http://xmlstar.sourceforge.net/docs.php
.
Validate one or more XML documents for well-formedness only:
xml validate {{path/to/input1.xml|URI}} {{input2.xml ...}}
Validate one or more XML documents against a Document Type Definition (DTD):
xml validate --dtd {{path/to/schema.dtd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}
Validate one or more XML documents against an XML Schema Definition (XSD):
xml validate --xsd {{path/to/schema.xsd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}
Validate one or more XML documents against a Relax NG schema (RNG):
xml validate --relaxng {{path/to/schema.rng}} {{path/to/input1.xml|URI}} {{input2.xml ...}}
Display help for the
validate
subcommand:
xml validate --help
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
