# iconv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/iconv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bvnc
,
sendmail
,
kind
,
join
,
tex
,
jhsdb
.
iconv
Converts text from one encoding to another.
More information:
https://manned.org/iconv
.
Convert file to a specific encoding, and print to stdout:
iconv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}
Convert file to the current locale's encoding, and output to a file:
iconv -f {{from_encoding}} {{input_file}} > {{output_file}}
List supported encodings:
iconv -l
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
