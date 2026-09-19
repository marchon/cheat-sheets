# fold

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fold/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
speedtest cli
,
podman
,
ebook convert
.
fold
Wraps each line in an input file to fit a specified width and prints it to the standard output.
More information:
https://www.gnu.org/software/coreutils/fold
.
Wrap each line to default width (80 characters):
fold {{file}}
Wrap each line to width "30":
fold -w30 {{file}}
Wrap each line to width "5" and break the line at spaces (puts each space separated word in a new line, words with length > 5 are wrapped):
fold -w5 -s {{file}}
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
