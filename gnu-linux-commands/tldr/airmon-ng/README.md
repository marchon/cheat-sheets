# airmon-ng

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/airmon-ng/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sum
,
transcode
,
r2
,
ia
,
route
,
renice
.
airmon-ng
Activate monitor mode on wireless network devices.
More information:
https://www.aircrack-ng.org/doku.php?id=airmon-ng
.
List wireless devices and their statuses:
sudo airmon-ng
Turn on monitor mode for a specific device:
sudo airmon-ng start {{wlan0}}
Kill disturbing processes that use wireless devices:
sudo airmon-ng check kill
Turn off monitor mode for a specific network interface:
sudo airmon-ng stop {{wlan0mon}}
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
