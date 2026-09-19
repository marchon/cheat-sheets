# transcode

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/transcode/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pio lib
,
pip install
,
xml canonic
.
transcode
Transcode video and audio codecs, and convert between media formats.
More information:
https://manned.org/transcode
.
Create stabilization file to be able to remove camera shakes:
transcode -J stabilize -i {{input_file}}
Remove camera shakes after creating stabilization file, transform video using XviD:
transcode -J transform -i {{input_file}} -y xvid -o {{output_file}}
Resize the video to 640x480 pixels and convert to MPEG4 codec using XviD:
transcode -Z 640x480 -i {{input_file}} -y xvid -o {{output_file}}
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
