# zeek

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zeek/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mongo
,
cosign
,
msfvenom
,
import
.
zeek
Passive network traffic analyzer.
Any output and log files will be saved to the current working directory.
More information:
https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility
.
Analyze live traffic from a network interface:
sudo zeek --iface {{interface}}
Analyze live traffic from a network interface and load custom scripts:
sudo zeek --iface {{interface}} {{script1}} {{script2}}
Analyze live traffic from a network interface, without loading any scripts:
sudo zeek --bare-mode --iface {{interface}}
Analyze live traffic from a network interface, applying a
tcpdump
filter:
sudo zeek --filter {{path/to/filter}} --iface {{interface}}
Analyze live traffic from a network interface using a watchdog timer:
sudo zeek --watchdog --iface {{interface}}
Analyze traffic from a
pcap
file:
zeek --readfile {{path/to/file.trace}}
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
