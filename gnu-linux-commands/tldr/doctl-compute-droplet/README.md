# doctl-compute-droplet

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/doctl-compute-droplet/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh auth
,
pueue switch
,
gpg2
,
hakyll init
.
doctl compute droplet
List, create, and delete virtual machines which are called droplets.
More information:
https://docs.digitalocean.com/reference/doctl/reference/compute/droplet/
.
Create a droplet:
doctl compute droplet create --region {{region}} --image {{os_image}} --size {{vps_type}} {{droplet_name}}
Delete a droplet:
doctl compute droplet delete {{droplet_id|droplet_name}}
List droplets:
doctl compute droplet list
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
