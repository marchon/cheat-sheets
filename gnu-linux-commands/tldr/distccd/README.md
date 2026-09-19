# distccd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/distccd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
csslint
,
stripe
,
fortune
,
joe
,
virsh undefine
.
distccd
Server daemon for the distcc distributed compiler.
More information:
https://distcc.github.io
.
Start a daemon with the default settings:
distccd --daemon
Start a daemon, accepting connections from IPv4 private network ranges:
distccd --daemon --allow-private
Start a daemon, accepting connections from a specific network address or address range:
distccd --daemon --allow {{ip_address|network_prefix}}
Start a daemon with a lowered priority that can run a maximum of 4 tasks at a time:
distccd --daemon --jobs {{4}} --nice {{5}}
Start a daemon and register it via mDNS/DNS-SD (Zeroconf):
distccd --daemon --zeroconf
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
