# asciidoctor

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/asciidoctor/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fast
,
expand
,
rubocop
,
crystal
.
asciidoctor
A processor that converts AsciiDoc files to a publishable format.
More information:
https://docs.asciidoctor.org
.
Convert a specific
.adoc
file to HTML (the default output format):
asciidoctor {{path/to/file.adoc}}
Convert a specific
.adoc
file to HTML and link a CSS stylesheet:
asciidoctor -a stylesheet={{path/to/stylesheet.css}} {{path/to/file.adoc}}
Convert a specific
.adoc
file to embeddable HTML, removing everything except the body:
asciidoctor --embedded {{path/to/file.adoc}}
Convert a specific
.adoc
file to a PDF using the
asciidoctor-pdf
library:
asciidoctor --backend={{pdf}} --require={{asciidoctor-pdf}} {{path/to/file.adoc}}
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
