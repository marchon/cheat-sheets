# mp4box

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mp4box/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nload
,
git cp
,
convert
,
nvm.fish
.
mp4box
MPEG-4 Systems Toolbox - Muxes streams into MP4 container.
More information:
https://gpac.wp.imt.fr/mp4box
.
Display information about an existing MP4 file:
mp4box -info {{filename}}
Add an SRT subtitle file into an MP4 file:
mp4box -add {{input_subs.srt}}:lang=eng -add {{input.mp4}} {{output.mp4}}
Combine audio from one file and video from another:
mp4box -add {{input1.mp4}}#audio -add {{input2.mp4}}#video {{output.mp4}}
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
