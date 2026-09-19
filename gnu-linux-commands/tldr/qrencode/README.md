# qrencode

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/qrencode/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git rename remote
,
feh
,
ln
,
git pull
.
qrencode
QR Code generator. Supports PNG and EPS.
More information:
https://fukuchi.org/works/qrencode
.
Convert a string to a QR code and save to an output file:
qrencode -o {{path/to/output_file.png}} {{string}}
Convert an input file to a QR code and save to an output file:
qrencode -o {{path/to/output_file.png}} -r {{path/to/input_file}}
Convert a string to a QR code and print it in terminal:
qrencode -t ansiutf8 {{string}}
Convert input from pipe to a QR code and print it in terminal:
echo {{string}} | qrencode -t ansiutf8
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
