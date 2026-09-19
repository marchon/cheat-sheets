# kind

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kind/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pwgen
,
emacsclient
,
mp4box
,
clamdscan
.
kind
Tool for running local Kubernetes clusters using Docker container "nodes".
Designed for testing Kubernetes itself, but may be used for local development or continuous integration.
More information:
https://github.com/kubernetes-sigs/kind
.
Create a local Kubernetes cluster:
kind create cluster --name {{cluster_name}}
Delete one or more clusters:
kind delete clusters {{cluster_name}}
Get details about clusters, nodes, or the kubeconfig:
kind get {{clusters|nodes|kubeconfig}}
Export the kubeconfig or the logs:
kind export {{kubeconfig|logs}}
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
