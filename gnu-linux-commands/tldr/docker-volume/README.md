# docker-volume

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-volume/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ffmpeg
,
pypy
,
notmuch
,
jhsdb
,
umount
.
docker volume
Manage Docker volumes.
More information:
https://docs.docker.com/engine/reference/commandline/volume/
.
Create a volume:
docker volume create {{volume_name}}
Create a volume with a specific label:
docker volume create --label {{label}} {{volume_name}}
Create a
tmpfs
volume a size of 100 MiB and an uid of 1000:
docker volume create --opt {{type}}={{tmpfs}} --opt {{device}}={{tmpfs}} --opt {{o}}={{size=100m,uid=1000}} {{volume_name}}
List all volumes:
docker volume ls
Remove a volume:
docker volume rm {{volume_name}}
Display information about a volume:
docker volume inspect {{volume_name}}
Remove all unused local volumes:
docker volume prune
Display help for a subcommand:
docker volume {{subcommand}} --help
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
