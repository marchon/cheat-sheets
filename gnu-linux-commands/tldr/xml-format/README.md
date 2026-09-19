# xml-format

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xml-format/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ffmpeg
,
pueue restart
,
forever
.
xml format
Format an XML document.
More information:
http://xmlstar.sourceforge.net/docs.php
.
Format an XML document, indenting with tabs:
xml format --indent-tab {{path/to/input.xml|URI}} > {{path/to/output.xml}}
Format an HTML document, indenting with 4 spaces:
xml format --html --indent-spaces {{4}} {{path/to/input.html|URI}} > {{path/to/output.html}}
Recover parsable parts of a malformed XML document, without indenting:
xml format --recover --noindent {{path/to/malformed.xml|URI}} > {{path/to/recovered.xml}}
Format an XML document from stdin, removing the
DOCTYPE
declaration:
cat {{path\to\input.xml}} | xml format --dropdtd > {{path/to/output.xml}}
Format an XML document, omitting the XML declaration:
xml format --omit-decl {{path\to\input.xml|URI}} > {{path/to/output.xml}}
Display help for the
format
subcommand:
xml format --help
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
