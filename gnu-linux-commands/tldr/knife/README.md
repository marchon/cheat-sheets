# knife

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/knife/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nativefier
,
roave backward compatibility check
.
knife
CLI for interacting with a Chef server from a local Chef repo.
More information:
https://docs.chef.io/knife.html
.
Bootstrap a new node:
knife bootstrap {{fqdn_or_ip}}
List all registered nodes:
knife node list
Show a node:
knife node show {{node_name}}
Edit a node:
knife node edit {{node_name}}
Edit a role:
knife role edit {{role_name}}
View a data bag:
knife data bag show {{data_bag_name}} {{data_bag_item}}
Upload a local cookbook to the Chef server:
knife cookbook upload {{cookbook_name}}
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
