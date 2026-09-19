# gitlab-runner

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gitlab-runner/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
openssl ts
,
rev
,
base64
,
git config
.
gitlab-runner
CLI tool for managing GitLab runners.
More information:
https://docs.gitlab.com/runner/
.
Register a runner:
sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}}
Register a runner with a Docker executor:
sudo gitlab-runner register --url {{https://gitlab.example.com}} --registration-token {{token}} --name {{name}} --executor {{docker}}
Unregister a runner:
sudo gitlab-runner unregister --name {{name}}
Display the status of the runner service:
sudo gitlab-runner status
Restart the runner service:
sudo gitlab-runner restart
Check if the registered runners can connect to GitLab:
sudo gitlab-runner verify
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
