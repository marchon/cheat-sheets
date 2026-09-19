# kubectl-delete

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kubectl-delete/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
omf
,
carbon now
,
csvsort
,
assimp
.
kubectl delete
Delete Kubernetes resources.
More information:
https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete
.
Delete a specific pod:
kubectl delete pod {{pod_name}}
Delete a specific deployment:
kubectl delete deployment {{deployment_name}}
Delete a specific node:
kubectl delete node {{node_name}}
Delete all pods in a specified namespace:
kubectl delete pods --all --namespace {{namespace}}
Delete all deployments and services in a specified namespace:
kubectl delete deployments,services --all --namespace {{namespace}}
Delete all nodes:
kubectl delete nodes --all
Delete resources defined in a YAML manifest:
kubectl delete --filename {{path/to/manifest.yaml}}
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
