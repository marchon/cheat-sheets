# peerflix

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/peerflix/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
awk
,
7z
,
rc
,
odps func
,
direnv
,
grep
.
peerflix
Stream video- or audio-based torrents to a media player.
More information:
https://github.com/mafintosh/peerflix
.
Stream the largest media file in a torrent:
peerflix "{{torrent_url|magnet_link}}"
List all streamable files contained in a torrent (given as a magnet link):
peerflix "{{magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567}}" --list
Stream the largest file in a torrent, given as a torrent URL, to VLC:
peerflix "{{http://example.net/music.torrent}}" --vlc
Stream the largest file in a torrent to MPlayer, with subtitles:
peerflix "{{torrent_url|magnet_link}}" --mplayer --subtitles {{subtitle-file.srt}}
Stream all files from a torrent to Airplay:
peerflix "{{torrent_url|magnet_link}}" --all --airplay
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
