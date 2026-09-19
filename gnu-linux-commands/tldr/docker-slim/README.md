# docker-slim

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-slim/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
arch
,
rtmpdump
,
dvc dag
,
brew cask
.
docker-slim
Analyze and optimize Docker images.
More information:
https://github.com/docker-slim/docker-slim
.
Start DockerSlim on interactive mode:
docker-slim
Analyze Docker layers from a specific image:
docker-slim xray --target {{image:tag}}
Lint a Dockerfile:
docker-slim lint --target {{path/to/Dockerfile}}
Analyze and generate an optimized Docker image:
docker-slim build {{image:tag}}
Display help for a subcommand:
docker-slim {{subcommand}} --help
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
