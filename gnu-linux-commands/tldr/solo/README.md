# solo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/solo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
npm
,
neofetch
,
ftp
,
fastmod
,
dirname
.
solo
Interact with Solo hardware security keys.
More information:
https://github.com/solokeys/solo-python
.
List connected Solos:
solo ls
Update the currently connected Solo's firmware to the latest version:
solo key update
Blink the LED of a specific Solo:
solo key wink --serial {{serial_number}}
Generate random bytes using the currently connected Solo's secure random number generator:
solo key rng raw
Monitor the serial output of a Solo:
solo monitor {{path/to/serial_port}}
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
