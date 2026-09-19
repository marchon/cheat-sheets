# kubectl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kubectl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git rename tag
,
git clean
,
emulator
.
kubectl
Command-line interface for running commands against Kubernetes clusters.
Some subcommands such as
kubectl run
have their own usage documentation.
More information:
https://kubernetes.io/docs/reference/kubectl/
.
List information about a resource with more details:
kubectl get {{pod|service|deployment|ingress|...}} -o wide
Update specified pod with the label 'unhealthy' and the value 'true':
kubectl label pods {{name}} unhealthy=true
List all resources with different types:
kubectl get all
Display resource (CPU/Memory/Storage) usage of nodes or pods:
kubectl top {{pod|node}}
Print the address of the master and cluster services:
kubectl cluster-info
Display an explanation of a specific field:
kubectl explain {{pods.spec.containers}}
Print the logs for a container in a pod or specified resource:
kubectl logs {{pod_name}}
Run command in an existing pod:
kubectl exec {{pod_name}} -- {{ls /}}
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
