# nms

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nms/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git clean
,
git prune
,
axel
,
pueue edit
.
nms
Command-line tool that recreates the famous data decryption effect seen in the 1992 movie Sneakers from stdin.
More information:
https://github.com/bartobri/no-more-secrets
.
Decrypt text after a keystroke:
echo "{{Hello, World!}}" | nms
Decrypt output immediately, without waiting for a keystroke:
{{ls -la}} | nms -a
Decrypt the content of a file, with a custom output color:
cat {{path/to/file}} | nms -a -f {{blue|white|yellow|black|magenta|green|red}}
Clear the screen before decrypting:
{{command}} | nms -a -c
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
