# stolonctl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/stolonctl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git alias
,
flask
,
textql
,
ncmpcpp
.
stolonctl
CLI for Stolon, a cloud native PostgreSQL manager for PostgreSQL high availability.
More information:
https://github.com/sorintlab/stolon
.
Get cluster status:
stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} status
Get cluster data:
stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} clusterdata
Get cluster specification:
stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} spec
Update cluster specification with a patch in JSON format:
stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} update --patch '{{cluster_spec}}'
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
