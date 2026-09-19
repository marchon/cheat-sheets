# uuencode

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/uuencode/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
zellij
,
csvsort
,
hydra
,
xml edit
.
uuencode
Encode binary files into ASCII for transport via mediums that only support simple ASCII encoding.
More information:
https://manned.org/uuencode
.
Encode a file and print the result to stdout:
uuencode {{path/to/input_file}} {{output_file_name_after_decoding}}
Encode a file and write the result to a file:
uuencode -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}
Encode a file using Base64 instead of the default uuencode encoding and write the result to a file:
uuencode -m -o {{path/to/output_file}} {{path/to/input_file}} {{output_file_name_after_decoding}}
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
