# fluxctl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fluxctl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git show index
,
maestral
,
box
.
fluxctl
Command-line tool for Flux v1.
More information:
https://fluxcd.io/legacy/flux/references/fluxctl
.
List workloads currently running in the cluster on specific namespace:
fluxctl --k8s-fwd-ns={{namespace}} list-workloads
Show deployed and available images:
fluxctl list-images
Synchronize the cluster with the git repository:
fluxctl sync
Turn on automatic deployment for a workload:
fluxctl automate
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
