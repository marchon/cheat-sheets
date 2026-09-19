# etcdctl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/etcdctl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gmssl
,
neofetch
,
mpd
,
qr
,
act
,
doctl apps
.
etcdctl
CLI interface for interacting with etcd, a highly-available key-value pair store.
More information:
https://etcd.io/docs/latest/dev-guide/interacting_v3/
.
Display the value associated with a specified key:
etcdctl get {{my/key}}
Store a key-value pair:
etcdctl put {{my/key}} {{my_value}}
Delete a key-value pair:
etcdctl del {{my/key}}
Store a key-value pair, reading the value from a file:
etcdctl put {{my/file}} < {{path/to/file.txt}}
Save a snapshot of the etcd keystore:
etcdctl snapshot save {{path/to/snapshot.db}}
Restore a snapshot of an etcd keystore (restart the etcd server afterwards):
etcdctl snapshot restore {{path/to/snapshot.db}}
Add a user:
etcdctl user add {{my_user}}
Watch a key for changes:
etcdctl watch {{my/key}}
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
