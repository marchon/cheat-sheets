# gitlab-ctl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gitlab-ctl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
salt call
,
pre commit
,
license
.
gitlab-ctl
CLI tool for managing the GitLab omnibus.
More information:
https://docs.gitlab.com/omnibus/maintenance/
.
Display the status of every service:
sudo gitlab-ctl status
Display the status of a specific service:
sudo gitlab-ctl status {{nginx}}
Restart every service:
sudo gitlab-ctl restart
Restart a specific service:
sudo gitlab-ctl restart {{nginx}}
Display the logs of every service and keep reading until
Ctrl + C
is pressed:
sudo gitlab-ctl tail
Display the logs of a specific service:
sudo gitlab-ctl tail {{nginx}}
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
