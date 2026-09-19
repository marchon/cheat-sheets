# docker-swarm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-swarm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nix
,
hg serve
,
mosquitto
,
surfraw
.
docker swarm
A container orchestration tool.
More information:
https://docs.docker.com/engine/swarm/
.
Initialize a swarm cluster:
docker swarm init
Display the token to join a manager or a worker:
docker swarm join-token {{worker|manager}}
Join a new node to the cluster:
docker swarm join --token {{token}} {{manager_node_url:2377}}
Remove a worker from the swarm (run inside the worker node):
docker swarm leave
Display the current CA certificate in PEM format:
docker swarm ca
Rotate the current CA certificate and display the new certificate:
docker swarm ca --rotate
Change the valid period for node certificates:
docker swarm update --cert-expiry {{hours}}h{{minutes}}m{{seconds}}s
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
