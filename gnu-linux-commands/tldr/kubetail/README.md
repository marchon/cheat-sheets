# kubetail

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kubetail/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
stripe
,
starship
,
chezmoi
,
nimble
.
kubetail
Utility to tail multiple Kubernetes pod logs at the same time.
More information:
https://github.com/johanhaleby/kubetail
.
Tail the logs of multiple pods (whose name starts with "my_app") in one go:
kubetail {{my_app}}
Tail only a specific container from multiple pods:
kubetail {{my_app}} -c {{my_container}}
To tail multiple containers from multiple pods:
kubetail {{my_app}} -c {{my_container_1}} -c {{my_container_2}}
To tail multiple applications at the same time separate them by comma:
kubetail {{my_app_1}},{{my_app_2}}
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
