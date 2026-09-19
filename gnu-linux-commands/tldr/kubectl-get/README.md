# kubectl-get

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kubectl-get/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
killall
,
btm
,
msbuild
,
mysqld
,
last
.
kubectl get
Get Kubernetes objects and resources.
More information:
https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get
.
Get all namespaces in the current cluster:
kubectl get namespaces
Get nodes in a specified namespace:
kubectl get nodes -n {{namespace}}
Get pods in a specified namespace:
kubectl get pods -n {{namespace}}
Get deployments in a specified namespace:
kubectl get deployments -n {{namespace}}
Get services in a specified namespace:
kubectl get services -n {{namespace}}
Get all resources in a specified namespace:
kubectl get all -n {{namespace}}
Get Kubernetes objects defined in a YAML manifest:
kubectl get -f {{path/to/manifest}}.yaml
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
