# kubectl-describe

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kubectl-describe/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
objdump
,
semver
,
llvm g++
,
oc
,
vsce
.
kubectl describe
Show details of Kubernetes objects and resources.
More information:
https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe
.
Show details of pods in a namespace:
kubectl describe pods -n {{namespace}}
Show details of nodes in a namespace:
kubectl describe nodes -n {{namespace}}
Show the details of a specific pod in a namespace:
kubectl describe pods {{pod_name}} -n {{namespace}}
Show the details of a specific node in a namespace:
kubectl describe nodes {{node_name}} -n {{namespace}}
Show details of Kubernetes objects defined in a YAML manifest:
kubectl describe -f {{path/to/manifest}}.yaml
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
