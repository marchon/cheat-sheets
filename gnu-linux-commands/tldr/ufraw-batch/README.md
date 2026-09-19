# ufraw-batch

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ufraw-batch/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
p4
,
lzop
,
xml depyx
,
zola
,
lighthouse
.
ufraw-batch
Convert RAW files from cameras into standard image files.
More information:
https://manned.org/ufraw-batch
.
Simply convert RAW files to JPG:
ufraw-batch --out-type=jpg {{input_file(s)}}
Simply convert RAW files to PNG:
ufraw-batch --out-type=png {{input_file(s)}}
Extract the preview image from the raw file:
ufraw-batch --embedded-image {{input_file(s)}}
Save the file with size up to the given maximums MAX1 and MAX2:
ufraw-batch --size=MAX1,MAX2 {{input_file(s)}}
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
