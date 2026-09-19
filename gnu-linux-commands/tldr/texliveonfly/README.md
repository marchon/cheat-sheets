# texliveonfly

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/texliveonfly/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nix
,
musescore
,
go clean
,
carp
.
texliveonfly
Downloads missing TeX Live packages while compiling
.tex
files.
More information:
https://ctan.org/pkg/texliveonfly
.
Download missing packages while compiling:
texliveonfly {{source.tex}}
Use a specific compiler (defaults to
pdflatex
):
texliveonfly --compiler={{compiler}} {{source.tex}}
Use a custom TeX Live
bin
folder:
texliveonfly --texlive_bin={{path/to/texlive_bin}} {{source.tex}}
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
