# docker-service

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-service/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dep
,
emacs
,
gifsicle
,
theharvester
.
docker service
Manage the services on a docker daemon.
More information:
https://docs.docker.com/engine/reference/commandline/service/
.
List the services on a docker daemon:
docker service ls
Create a new service:
docker service create --name {{service_name}} {{image}}:{{tag}}
Display detailed information of a space-separated list of services:
docker service inspect {{service_name|ID}}
List the tasks of a space-separated list of services:
docker service ps {{service_name|ID}}
Scale to a specific number of replicas for a space-separated list of services:
docker service scale {{service_name}}={{count_of_replicas}}
Remove a space-separated list of services:
docker service rm {{service_name|ID}}
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
