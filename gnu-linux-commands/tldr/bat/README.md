# bat

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bat/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pueue switch
,
gv2gml
,
restic
.
bat
Print and concatenate files.
A
cat
clone with syntax highlighting and Git integration.
More information:
https://github.com/sharkdp/bat
.
Print the contents of a file to the standard output:
bat {{file}}
Concatenate several files into the target file:
bat {{file1}} {{file2}} > {{target_file}}
Append several files into the target file:
bat {{file1}} {{file2}} >> {{target_file}}
Number all output lines:
bat -n {{file}}
Syntax highlight a JSON file:
bat --language json {{file.json}}
Display all supported languages:
bat --list-languages
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
