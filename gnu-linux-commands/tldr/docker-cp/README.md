# docker-cp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/docker-cp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
odps inst
,
trans
,
circup
,
cradle
.
docker cp
Copy files or directories between host and container filesystems.
More information:
https://docs.docker.com/engine/reference/commandline/cp
.
Copy a file or directory from the host to a container:
docker cp {{path/to/file_or_directory_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}
Copy a file or directory from a container to the host:
docker cp {{container_name}}:{{path/to/file_or_directory_in_container}} {{path/to/file_or_directory_on_host}}
Copy a file or directory from the host to a container, following symlinks (copies the symlinked files directly, not the symlinks themselves):
docker cp --follow-link {{path/to/symlink_on_host}} {{container_name}}:{{path/to/file_or_directory_in_container}}
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
