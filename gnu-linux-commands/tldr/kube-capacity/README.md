# kube-capacity

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kube-capacity/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git locked
,
git notes
,
zbarimg
.
kube-capacity
A simple CLI that provides an overview of the resource requests, limits, and utilization in a Kubernetes cluster.
Combine the best parts of
kubectl top
and
kubectl describe
into a CLI focused on cluster resources.
More information:
https://github.com/robscott/kube-capacity
.
Output a list of nodes with the total CPU and Memory resource requests and limits:
kube-capacity
Include pods:
kube-capacity -p
Include utilization:
kube-capacity -u
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
