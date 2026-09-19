# sponge

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sponge/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
asciidoctor
,
guacd
,
yesod
,
turbo
.
sponge
Soak up the input before writing the output file.
More information:
https://manned.org/sponge
.
Append file content to the source file:
cat {{path/to/file}} | sponge -a {{path/to/file}}
Remove all lines starting with # in a file:
grep -v '^{{#}}' {{path/to/file}} | sponge {{path/to/file}}
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
