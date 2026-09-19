# docker-inspect

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-inspect/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
stow
,
php coveralls
,
mpc
,
virsh pool list
.
docker inspect
Return low-level information on Docker objects.
More information:
https://docs.docker.com/engine/reference/commandline/inspect/
.
Show help:
docker inspect
Display information about a container, image, or volume using a name or ID:
docker inspect {{container|image|ID}}
Display a container's IP address:
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {{container}}
Display the path to the container's log file:
docker inspect --format='{{.LogPath}}' {{container}}
Display the image name of the container:
docker inspect --format='{{.Config.Image}}' {{container}}
Display the configuration information as JSON:
docker inspect --format='{{json .Config}}' {{container}}
Display all port bindings:
docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' {{container}}
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
