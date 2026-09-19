# etcd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/etcd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pueue parallel
,
pg_dump
,
arc
.
etcd
A distributed, reliable key-value store for the most critical data of a distributed system.
More information:
https://etcd.io
.
Start a single-node etcd cluster:
etcd
Start a single-node etcd cluster, listening for client requests on a custom URL:
etcd --advertise-client-urls {{http://127.0.0.1:1234}} --listen-client-urls {{http://127.0.0.1:1234}}
Start a single-node etcd cluster with a custom name:
etcd --name {{my_etcd_cluster}}
Start a single-node etcd cluster with extensive metrics available at http://localhost:2379/debug/pprof/:
etcd --enable-pprof --metrics extensive
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
