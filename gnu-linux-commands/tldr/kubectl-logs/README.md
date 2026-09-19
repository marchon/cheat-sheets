# kubectl-logs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kubectl-logs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gt
,
export
,
transmission create
.
kubectl logs
Show logs for containers in a pod.
More information:
https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs
.
Show logs for a single-container pod:
kubectl logs {{pod_name}}
Show logs for a specified container in a pod:
kubectl logs --container {{container_name}} {{pod_name}}
Show logs for all containers in a pod:
kubectl logs --all-containers={{true}} {{pod_name}}
Stream pod logs:
kubectl logs --follow {{pod_name}}
Stream logs for a specified container in a pod:
kubectl logs --follow --container {{container_name}} {{pod_name}}
Show pod logs newer than a relative time like
10s
,
5m
, or
1h
:
kubectl logs --since={{relative_time}} {{pod_name}}
Show the 10 most recent logs in a pod:
kubectl logs --tail={{10}} {{pod_name}}
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
