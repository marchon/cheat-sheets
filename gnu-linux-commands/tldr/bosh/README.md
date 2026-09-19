# bosh

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bosh/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
jobs
,
guile
,
autoflake
,
lli
,
ifconfig
.
bosh
Command-line tool to deploy and manage the bosh director.
More information:
https://bosh.io/docs/cli-v2/
.
Create local alias for director:
bosh alias-env {{environment_name}} -e {{ip_address|url}} --ca-cert {{ca_certificate}}
List environments:
bosh environments
Log in to the director:
bosh login -e {{environment}}
List deployments:
bosh -e {{environment}} deployments
List environment virtual machines:
bosh -e {{environment}} vms -d {{deployment}}
Ssh into virtual machine:
bosh -e {{environment}} ssh {{virtual_machine}} -d {{deployment}}
Upload stemcell:
bosh -e {{environment}} upload-stemcell {{stemcell_file|url}}
Show current cloud config:
bosh -e {{environment}} cloud-config
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
