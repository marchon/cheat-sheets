# docker-compose

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-compose/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
salt run
,
tail
,
pgbench
,
git annex
.
docker-compose
Run and manage multi container docker applications.
More information:
https://docs.docker.com/compose/reference/
.
List all running containers:
docker-compose ps
Create and start all containers in the background using a
docker-compose.yml
file from the current directory:
docker-compose up -d
Start all containers, rebuild if necessary:
docker-compose up --build
Start all containers using an alternate compose file:
docker-compose --file {{path/to/file}} up
Stop all running containers:
docker-compose stop
Stop and remove all containers, networks, images, and volumes:
docker-compose down --rmi all --volumes
Follow logs for all containers:
docker-compose logs --follow
Follow logs for a specific container:
docker-compose logs --follow {{container_name}}
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
