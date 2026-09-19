# mkvmerge

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mkvmerge/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
npx
,
xcaddy
,
nmap
,
pio device
,
wat2wasm
.
mkvmerge
Merge and extract multimedia streams.
More information:
https://mkvtoolnix.download/doc/mkvmerge.html
.
Display information about a Matroska file:
mkvmerge --identify {{path/to/file.mkv}}
Extract the audio from track 1 of a specific file:
mkvextract tracks {{path/to/file.mkv}} {{1}}:{{path/to/output.webm}}
Extract the subtitle from track 3 of a specific file:
mkvextract tracks {{path/to/file.mkv}} {{3}}:{{path/to/subs.srt}}
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
