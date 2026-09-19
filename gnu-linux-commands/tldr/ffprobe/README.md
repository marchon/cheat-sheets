# ffprobe

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ffprobe/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
isisdl
,
bat
,
zipinfo
,
loadtest
.
ffprobe
Multimedia stream analyzer.
More information:
https://ffmpeg.org/ffprobe.html
.
Display all available stream info for a media file:
ffprobe -v error -show_entries {{input.mp4}}
Display media duration:
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}
Display the frame rate of a video:
ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}
Display the width or height of a video:
ffprobe -v error -select_streams v:0 -show_entries stream={{width|height}} -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}
Display the average bit rate of a video:
ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 {{input.mp4}}
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
