# yank

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/yank/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
updog
,
who
,
base32
,
dirs
,
wondershaper
.
yank
Read input from stdin and display a selection interface that allows a field to be selected and copied to the clipboard.
More information:
https://manned.org/yank
.
Yank using the default delimiters (\f, \n, \r, \s, \t):
{{sudo dmesg}} | yank
Yank an entire line:
{{sudo dmesg}} | yank -l
Yank using a specific delimiter:
{{echo hello=world}} | yank -d {{=}}
Only yank fields matching a specific pattern:
{{ps ux}} | yank -g "{{[0-9]+}}"
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
