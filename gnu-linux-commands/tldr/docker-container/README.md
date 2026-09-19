# docker-container

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-container/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pdfinfo
,
ping
,
az bicep
,
uvicorn
.
docker container
Manage Docker containers.
More information:
https://docs.docker.com/engine/reference/commandline/container/
.
List currently running Docker containers:
docker container ls
Start one or more stopped containers:
docker container start {{container1_name}} {{container2_name}}
Kill one or more running containers:
docker container kill {{container_name}}
Stop one or more running containers:
docker container stop {{container_name}}
Pause all processes within one or more containers:
docker container pause {{container_name}}
Display detailed information on one or more containers:
docker container inspect {{container_name}}
Export a container's filesystem as a tar archive:
docker container export {{container_name}}
Create a new image from a container's changes:
docker container commit {{container_name}}
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
