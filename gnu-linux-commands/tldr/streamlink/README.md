# streamlink

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/streamlink/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bootctl
,
runsvchdir
,
openssl dgst
.
streamlink
Extracts streams from various services and pipes them into a video player of choice.
More information:
https://streamlink.github.io
.
Attempt to extract streams from the URL specified, and if it's successful, print out a list of available streams to choose from:
streamlink {{example.com/stream}}
Open a stream with the specified quality:
streamlink {{example.com/stream}} {{720p60}}
Select the highest or lowest available quality:
streamlink {{example.com/stream}} {{best|worst}}
Specify which player to use to feed stream data to (VLC is used by default if found):
streamlink --player={{mpv}} {{example.com/stream}} {{best}}
Specify the amount of time to skip from the beginning of the stream. For live streams, this is a negative offset from the end of the stream (rewind):
streamlink --hls-start-offset {{[HH:]MM:SS}} {{example.com/stream}} {{best}}
Skip to the beginning of a live stream, or as far back as possible:
streamlink --hls-live-restart {{example.com/stream}} {{best}}
Write stream data to a file instead of playing it:
streamlink --output {{path/to/file.ts}} {{example.com/stream}} {{best}}
Open the stream in the player, while at the same time writing it to a file:
streamlink --record {{path/to/file.ts}} {{example.com/stream}} {{best}}
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
