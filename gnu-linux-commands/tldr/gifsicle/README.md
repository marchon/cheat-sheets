# gifsicle

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gifsicle/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
exiv2
,
script
,
alacritty
,
npm home
.
gifsicle
Create GIFs.
More information:
https://www.lcdf.org/gifsicle
.
Optimise a GIF:
gifsicle --batch --optimize=3 {{amin.gif}}
Make a GIF animation with gifsicle:
gifsicle --delay={{10}} --loop *.gif > {{anim.gif}}
Extract frames from an animation:
gifsicle {{anim.gif}} '#0' > {{firstframe.gif}}
You can also edit animations by replacing, deleting, or inserting frames:
gifsicle -b {{anim.gif}} --replace '#0' {{new.gif}}
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
