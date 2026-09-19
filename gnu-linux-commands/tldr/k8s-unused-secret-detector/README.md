# k8s-unused-secret-detector

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/k8s-unused-secret-detector/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
just
,
haxelib
,
snyk
,
env
,
httprobe
.
k8s-unused-secret-detector
Command-line interface tool for detecting unused Kubernetes secrets.
More information:
https://github.com/dtan4/k8s-unused-secret-detector
.
Detect unused secrets:
k8s-unused-secret-detector
Detect unused secrets in a specific namespace:
k8s-unused-secret-detector -n {{namespace}}
Delete unused secrets in a specific namespace:
k8s-unused-secret-detector -n {{namespace}} | kubectl delete secret -n {{namespace}}
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
