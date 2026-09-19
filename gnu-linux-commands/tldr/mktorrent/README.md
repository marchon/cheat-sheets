# mktorrent

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mktorrent/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dvc freeze
,
docker
,
neofetch
.
mktorrent
A CLI utility to create BitTorrent metainfo files.
More information:
https://github.com/Rudde/mktorrent
.
Create a torrent with 2^21 KB as the piece size:
mktorrent -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}
Create a private torrent with a 2^21 KB piece size:
mktorrent -p -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}
Create a torrent with a comment:
mktorrent -c "{{comment}}" -a {{tracker_announce_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}
Create a torrent with multiple trackers:
mktorrent -a {{tracker_announce_url,tracker_announce_url_2}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}
Create a torrent with web seed URLs:
mktorrent -a {{tracker_announce_url}} -w {{web_seed_url}} -l {{21}} -o {{path/to/example.torrent}} {{path/to/file_or_directory}}
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
