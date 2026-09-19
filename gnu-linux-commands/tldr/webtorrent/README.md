# webtorrent

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/webtorrent/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dolt commit
,
particle
,
go fix
.
webtorrent
The command-line interface for WebTorrent.
Supports magnets, URLs, info hashes and
.torrent
files.
More information:
https://github.com/webtorrent/webtorrent-cli
.
Download a torrent:
webtorrent download "{{torrent_id}}"
Stream a torrent to VLC media player:
webtorrent download "{{torrent_id}}" --vlc
Stream a torrent to a Digital Living Network Alliance (DLNA) device:
webtorrent download "{{torrent_id}}" --dlna
Display a list of files for a specific torrent:
webtorrent download "{{torrent_id}}" --select
Specify a file index from the torrent to download:
webtorrent download "{{torrent_id}}" --select {{index}}
Seed a specific file or directory:
webtorrent seed {{path/to/file_or_directory}}
Create a new torrent file for the specified file path:
webtorrent create {{path/to/file}}
Display information for a magnet URI or
.torrent
file:
webtorrent info {{path/to/file_or_magnet}}
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
