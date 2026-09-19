# docker-save

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-save/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
asdf
,
gh run
,
go env
,
glab mr merge
.
docker save
Export one or more docker images to archive.
More information:
https://docs.docker.com/engine/reference/commandline/save/
.
Save an image by redirecting stdout to a tar archive:
docker save {{image}}:{{tag}} > {{path/to/file.tar}}
Save an image to a tar archive:
docker save --output {{path/to/file.tar}} {{image}}:{{tag}}
Save all tags of the image:
docker save --output {{path/to/file.tar}} {{image_name}}
Cherry-pick particular tags of an image to save:
docker save --output {{path/to/file.tar}} {{image_name:tag1 image_name:tag2 ...}}
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
