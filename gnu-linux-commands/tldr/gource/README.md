# gource

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gource/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
asciinema
,
git clear soft
,
hexyl
.
gource
Renders an animated tree diagram of Git, SVN, Mercurial and Bazaar repositories.
It shows files and directories being created, modified or removed over time.
More information:
https://gource.io
.
Run gource in a directory (if it isn't the repository's root directory, the root is sought up from there):
gource {{path/to/repository}}
Run gource in the current directory, with a custom output resolution:
gource -{{width}}x{{height}}
Set a custom timescale for the animation:
gource -c {{time_scale_multiplier}}
Set how long each day should be in the animation (this combines with -c, if provided):
gource -s {{seconds}}
Set fullscreen mode and a custom background color:
gource -f -b {{hex_color_code}}
Set a title for the animation:
gource --title {{title}}
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
