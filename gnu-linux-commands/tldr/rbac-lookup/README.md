# rbac-lookup

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rbac-lookup/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
stolonctl
,
textql
,
npm why
,
az appconfig
.
rbac-lookup
Find roles and cluster roles attached to any user, service account or group name in your Kubernetes cluster.
More information:
https://github.com/reactiveops/rbac-lookup
.
View all RBAC bindings:
rbac-lookup
View RBAC bindings that match a given expression:
rbac-lookup {{search_term}}
View all RBAC bindings along with the source role binding:
rbac-lookup -o wide
View all RBAC bindings filtered by subject:
rbac-lookup -k {{user|group|serviceaccount}}
View all RBAC bindings along with IAM roles (if you are using GKE):
rbac-lookup --gke
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
