# base64

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/base64/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
date
,
virt clone
,
peerflix
,
gh auth
.
base64
Encode or decode file or standard input to/from Base64, to standard output.
More information:
https://www.gnu.org/software/coreutils/base64
.
Encode the contents of a file as base64 and write the result to stdout:
base64 {{filename}}
Decode the base64 contents of a file and write the result to stdout:
base64 --decode {{filename}}
Encode from stdin:
{{somecommand}} | base64
Decode from stdin:
{{somecommand}} | base64 --decode
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
