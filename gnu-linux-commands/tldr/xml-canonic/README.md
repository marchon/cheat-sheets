# xml-canonic

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xml-canonic/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mullvad
,
pest
,
httprobe
,
swc
,
cloc
.
xml canonic
Make XML documents canonical.
More information:
http://xmlstar.sourceforge.net/docs.php
.
Make an XML document canonical, preserving comments:
xml canonic {{path/to/input.xml|URI}} > {{path/to/output.xml}}
Make an XML document canonical, removing comments:
xml canonic --without-comments {{path/to/input.xml|URI}} > {{path/to/output.xml}}
Make XML exclusively canonical, using an XPATH from a file, preserving comments:
xml canonic --exc-with-comments {{path/to/input.xml|URI}} {{path/to/c14n.xpath}}
Display help for the
canonic
subcommand:
xml canonic --help
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
