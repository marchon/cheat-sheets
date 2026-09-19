# docker-login

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-login/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
encfs
,
pigz
,
git checkout index
.
docker login
Log into a docker registry.
More information:
https://docs.docker.com/engine/reference/commandline/login/
.
Interactively log into a registry:
docker login
Log into a registry with a specific username (user will be prompted for a password):
docker login --username {{username}}
Log into a registry with username and password:
docker login --username {{username}} --password {{password}} {{server}}
Log into a registry with password from stdin:
echo "{{password}}" | docker login --username {{username}} --password-stdin
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
