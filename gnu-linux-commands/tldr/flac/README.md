# flac

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/flac/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kustomize
,
yq
,
dig
,
dlv
,
wondershaper
.
flac
Encodes, decodes and tests FLAC files.
More information:
https://xiph.org/flac
.
Encode a WAV file to FLAC (this will create a FLAC file in the same location as the WAV file):
flac {{path/to/file.wav}}
Encode a WAV file to FLAC, specifying the output file:
flac -o {{path/to/output.flac}} {{path/to/file.wav}}
Decode a FLAC file to WAV, specifying the output file:
flac -d -o {{path/to/output.wav}} {{path/to/file.flac}}
Test a FLAC file for the correct encoding:
flac -t {{path/to/file.flac}}
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
