# tailscale

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tailscale/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
kiwi ng
,
acme.sh
,
shiori
,
trivy
.
tailscale
A private WireGuard network service.
Some subcommands such as
tailscale up
have their own usage documentation.
More information:
https://tailscale.com
.
Connect to Tailscale:
sudo tailscale up
Disconnect from Tailscale:
sudo tailscale down
Display the current Tailscale IP addresses:
tailscale ip
Ping a peer node at the Tailscale layer and display which route it took for each response:
tailscale ping {{ip|hostname}}
Analyze the local network conditions and display the result:
tailscale netcheck
Start a web server for controlling Tailscale:
tailscale web
Display a shareable identifier to help diagnose issues:
tailscale bugreport
Display help for a subcommand:
tailscale {{subcommand}} --help
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
