# kubeadm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kubeadm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fmt
,
pfetch
,
git reset file
,
exiv2
.
kubeadm
Command-line interface for creating and managing Kubernetes clusters.
More information:
https://kubernetes.io/docs/reference/setup-tools/kubeadm
.
Create a Kubernetes master node:
kubeadm init
Bootstrap a Kubernetes worker node and join it to a cluster:
kubeadm join --token {{token}}
Create a new bootstrap token with a TTL of 12 hours:
kubeadm token create --ttl {{12h0m0s}}
Check if the Kubernetes cluster is upgradeable and which versions are available:
kubeadm upgrade plan
Upgrade Kubernetes cluster to a specified version:
kubeadm upgrade apply {{version}}
View the kubeadm ConfigMap containing the cluster's configuration:
kubeadm config view
Revert changes made to the host by 'kubeadm init' or 'kubeadm join':
kubeadm reset
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
