# pandoc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pandoc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
multitail
,
llvm gcc
,
hostapd
.
pandoc
Convert documents between various formats.
More information:
https://pandoc.org
.
Convert file to PDF (the output format is determined by file extension):
pandoc {{input.md}} -o {{output.pdf}}
Force conversion to use a specific format:
pandoc {{input.docx}} --to {{gfm}} -o {{output.md}}
Convert to a standalone file with the appropriate headers/footers (for LaTeX, HTML, etc.):
pandoc {{input.md}} -s -o {{output.tex}}
List all supported input formats:
pandoc --list-input-formats
List all supported output formats:
pandoc --list-output-formats
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
