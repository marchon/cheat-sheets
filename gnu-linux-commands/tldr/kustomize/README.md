# kustomize

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kustomize/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
multitail
,
tuir
,
jest
,
pip install
.
kustomize
Kustomize is a tool to easily deploy resources for Kubernetes.
More information:
https://github.com/kubernetes-sigs/kustomize
.
Create kustomization file with resources and namespace:
kustomize create --resources {{deployment.yaml,service.yaml}} --namespace {{staging}}
Build kustomization file and deploy it with
kubectl
:
kustomize build . | kubectl apply -f -
Set an image in the kustomization file:
kustomize edit set image {{busybox=alpine:3.6}}
Search for Kubernetes resources in the current directory to be added to the kustomization file:
kustomize create --autodetect
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
