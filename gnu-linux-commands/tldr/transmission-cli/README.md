# transmission-cli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/transmission-cli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
samtools
,
gh codespace
,
amass
.
transmission-cli
A lightweight, command-line BitTorrent client.
This tool has been deprecated, please see
transmission-remote
.
More information:
https://transmissionbt.com
.
Download a specific torrent:
transmission-cli {{url|magnet|path/to/file}}
Download a torrent to a specific directory:
transmission-cli --download-dir {{path/to/download_directory}} {{url|magnet|path/to/file}}
Create a torrent file from a specific file or directory:
transmission-cli --new {{path/to/source_file_or_directory}}
Set the download speed limit to 50 KB/s:
transmission-cli --downlimit {{50}} {{url|magnet|path/to/file}}
Set the upload speed limit to 50 KB/s:
transmission-cli --uplimit {{50}} {{url|magnet|path/to/file}}
Use a specific port for connections:
transmission-cli --port {{port_number}} {{url|magnet|path/to/file}}
Force encryption for peer connections:
transmission-cli --encryption-required {{url|magnet|path/to/file}}
Use a Bluetack-formatted peer blocklist:
transmission-cli --blocklist {{blocklist_url|path/to/blocklist}} {{url|magnet|path/to/file}}
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
