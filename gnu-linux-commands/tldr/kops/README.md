# kops

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kops/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vim
,
mh_metric
,
stat
,
pio update
.
kops
Create, destroy, upgrade and maintain Kubernetes clusters from the command-line.
More information:
https://github.com/kubernetes/kops/
.
Create a cluster from the configuration specification:
kops create cluster -f {{cluster_name.yaml}}
Create a new ssh public key:
kops create secret sshpublickey {{key_name}} -i {{~/.ssh/id_rsa.pub}}
Export the cluster configuration to the
~/.kube/config
file:
kops export kubecfg {{cluster_name}}
Get the cluster configuration as YAML:
kops get cluster {{cluster_name}} -o yaml
Delete a cluster:
kops delete cluster {{cluster_name}} --yes
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
