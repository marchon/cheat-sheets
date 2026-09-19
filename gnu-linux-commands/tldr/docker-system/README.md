# docker-system

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-system/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
roave backward compatibility check
.
docker system
Manage Docker data and display system-wide information.
More information:
https://docs.docker.com/engine/reference/commandline/system/
.
Show help:
docker system
Show docker disk usage:
docker system df
Show detailed information on disk usage:
docker system df --verbose
Remove unused data:
docker system prune
Remove unused data created more than a specified amount of time in the past:
docker system prune --filter="until={{hours}}h{{minutes}}m"
Display real-time events from the Docker daemon:
docker system events
Display real-time events from containers streamed as valid JSON Lines:
docker system events --filter 'type=container' --format '{{json .}}'
Display system-wide information:
docker system info
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
