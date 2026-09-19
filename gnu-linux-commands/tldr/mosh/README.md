# mosh

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mosh/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ansible doc
,
gimp
,
drill
,
flyctl
.
mosh
Mobile Shell (
mosh
) is a robust and responsive replacement for SSH.
mosh
persists connections to remote servers while roaming between networks.
More information:
https://mosh.org
.
Connect to a remote server:
mosh {{username}}@{{remote_host}}
Connect to a remote server with a specific identity (private key):
mosh --ssh="ssh -i {{path/to/key_file}}" {{username}}@{{remote_host}}
Connect to a remote server using a specific port:
mosh --ssh="ssh -p {{2222}}" {{username}}@{{remote_host}}
Run a command on a remote server:
mosh {{remote_host}} -- {{command -with -flags}}
Select Mosh UDP port (useful when
{{remote_host}}
is behind a NAT):
mosh -p {{124}} {{username}}@{{remote_host}}
Usage when
mosh-server
binary is outside standard path:
mosh --server={{path/to/bin/}}mosh-server {{remote_host}}
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
