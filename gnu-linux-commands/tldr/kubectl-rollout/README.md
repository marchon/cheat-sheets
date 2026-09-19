# kubectl-rollout

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kubectl-rollout/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
thunderbird
,
make
,
tlmgr remove
.
kubectl rollout
Manage the rollout of a Kubernetes resource (deployments, daemonsets, and statefulsets).
More information:
https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout
.
Start a rolling restart of a resource:
kubectl rollout restart {{resource_type}}/{{resource_name}}
Watch the rolling update status of a resource:
kubectl rollout status {{resource_type}}/{{resource_name}}
Roll back a resource to the previous revision:
kubectl rollout undo {{resource_type}}/{{resource_name}}
View the rollout history of a resource:
kubectl rollout history {{resource_type}}/{{resource_name}}
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
