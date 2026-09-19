# feh

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/feh/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dotnet ef
,
sh
,
java
,
tee
,
kops
,
docker system
.
feh
Lightweight image viewing utility.
More information:
https://feh.finalrewind.org
.
View images locally or using a URL:
feh {{path/to/images}}
View images recursively:
feh --recursive {{path/to/images}}
View images without window borders:
feh --borderless {{path/to/images}}
Exit after the last image:
feh --cycle-once {{path/to/images}}
Set the slideshow cycle delay:
feh --slideshow-delay {{seconds}} {{path/to/images}}
Set your wallpaper (centered, filled, maximized, scaled or tiled):
feh --bg-{{center|fill|max|scale|tile}} {{path/to/image}}
Create a montage of all images within a directory. Outputs as a new image:
feh --montage --thumb-height {{150}} --thumb-width {{150}} --index-info "{{%nn%wx%h}}" --output {{path/to/montage_image.png}}
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
