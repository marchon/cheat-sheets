# doctl-apps

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/doctl-apps/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ifconfig
,
smbmap
,
moe
,
protoc
,
uniq
.
doctl apps
Used to manage digitalocean apps.
More information:
https://docs.digitalocean.com/reference/doctl/reference/apps
.
Create an app:
doctl apps create
Create a deployment for a specific app:
doctl apps create-deployment {{app_id}}
Delete an app interactively:
doctl apps delete {{app_id}}
Get an app:
doctl apps get
List all apps:
doctl apps list
List all deployments from a specific app:
doctl apps list-deployments {{app_id}}
Get logs from a specific app:
doctl apps logs {{app_id}}
Update a specific app with a given app spec:
doctl apps update {{app_id}} --spec {{path/to/spec.yml}}
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
