# inkmake

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/inkmake/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sk
,
tlmgr update
,
shiori
,
dep
,
makensis
.
inkmake
GNU Makefile-style SVG exporting using Inkscape's backend.
More information:
https://github.com/wader/inkmake
.
Export an SVG file executing the specified Inkfile:
inkmake {{path/to/Inkfile}}
Execute an Inkfile and show detailed information:
inkmake --verbose {{path/to/Inkfile}}
Execute an Inkfile, specifying SVG input file(s) and an output file:
inkmake --svg {{path/to/file.svg}} --out {{path/to/output_image}} {{path/to/Inkfile}}
Specify a custom Inkscape binary to use as the backend:
inkmake --inkscape {{/Applications/Inkscape.app/Contents/Resources/bin/inkscape}} {{path/to/Inkfile}}
Display help:
inkmake --help
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
