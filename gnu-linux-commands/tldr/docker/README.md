# docker

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
runsv
,
newman
,
nimble
,
jtbl
,
expr
.
docker
Manage Docker containers and images.
Some subcommands such as
docker run
have their own usage documentation.
More information:
https://docs.docker.com/engine/reference/commandline/cli/
.
List all docker containers (running and stopped):
docker ps --all
Start a container from an image, with a custom name:
docker run --name {{container_name}} {{image}}
Start or stop an existing container:
docker {{start|stop}} {{container_name}}
Pull an image from a docker registry:
docker pull {{image}}
Display the list of already downloaded images:
docker images
Open a shell inside a running container:
docker exec -it {{container_name}} {{sh}}
Remove a stopped container:
docker rm {{container_name}}
Fetch and follow the logs of a container:
docker logs -f {{container_name}}
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
