# enscript

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/enscript/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vagrant
,
dust
,
keychain
,
ngs
,
openssl
.
enscript
Convert text files to PostScript, HTML, RTF, ANSI, and overstrikes.
More information:
https://www.gnu.org/software/enscript
.
Generate a PostScript file from a text file:
enscript {{path/to/input_file}} --output={{path/to/output_file}}
Generate a file in a different language than PostScript:
enscript {{path/to/input_file}} --language={{html|rtf|...}} --output={{path/to/output_file}}
Generate a PostScript file with a landscape layout, splitting the page into columns (maximum 9):
enscript {{path/to/input_file}} --columns={{num}} --landscape --output={{path/to/output_file}}
Display available syntax highlighting languages and file formats:
enscript --help-highlight
Generate a PostScript file with syntax highlighting and color for a specified language:
enscript {{path/to/input_file}} --color=1 --highlight={{language}} --output={{path/to/output_file}}
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
