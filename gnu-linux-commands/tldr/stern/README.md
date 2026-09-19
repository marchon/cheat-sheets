# stern

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/stern/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
qdbus
,
swipl
,
calibre server
.
stern
Tail multiple pods and containers from Kubernetes.
More information:
https://github.com/wercker/stern/
.
Tail all pods within a current namespace:
stern .
Tail all pods with a specific status:
stern . --container-state {{running|waiting|terminated}}
Tail all pods that matches a given regular expression:
stern {{pod_query}}
Tail matched pods from all namespaces:
stern {{pod_query}} --all-namespaces
Tail matched pods from 15 minutes ago:
stern {{pod_query}} --since {{15m}}
Tail matched pods with a specific label:
stern {{pod_query}} --selector {{release=canary}}
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
