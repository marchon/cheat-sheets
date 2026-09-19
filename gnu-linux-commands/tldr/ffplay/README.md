# ffplay

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ffplay/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
smbmap
,
bash it
,
gitmoji
,
wait
.
ffplay
A simple and portable media player using the FFmpeg libraries and the SDL library.
More information:
https://ffmpeg.org/ffplay-all.html
.
Play a media file:
ffplay {{path/to/file}}
Play a video and show motion vectors in real time:
ffplay -flags2 +export_mvs -vf codecview=mv=pf+bf+bb {{path/to/file}}
Show only video keyframes:
ffplay -vf select="{{eq(pict_type\,PICT_TYPE_I)}}" {{path/to/file}}
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
