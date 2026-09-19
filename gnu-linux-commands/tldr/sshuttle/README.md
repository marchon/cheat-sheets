# sshuttle

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sshuttle/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aws ecr
,
theharvester
,
git stash
.
sshuttle
Transparent proxy server that tunnels traffic over an SSH connection.
Doesn't require root or any special setup on the remote SSH server, though root access on the local machine is prompted for.
More information:
https://manned.org/sshuttle
.
Forward all IPv4 TCP traffic via a remote SSH server:
sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}
Also forward all DNS traffic to the server's default DNS resolver:
sshuttle --dns --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}
Forward all traffic except that which is bound for a specific subnet:
sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} --exclude {{192.168.0.1/24}}
Use the tproxy method to forward all IPv4 and IPv6 traffic:
sshuttle --method=tproxy --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} {{::/0}} --exclude={{your_local_ip_address}} --exclude={{ssh_server_ip_address}}
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
