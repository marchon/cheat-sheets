# st-flash

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/st-flash/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git verify tag
,
bat
,
which
,
dlv
.
st-flash
Flash binary files to STM32 ARM Cortex microcontrollers.
More information:
https://github.com/texane/stlink
.
Read 4096 bytes from the device starting from 0x8000000:
st-flash read {{firmware}}.bin {{0x8000000}} {{4096}}
Write firmware to device starting from 0x8000000:
st-flash write {{firmware}}.bin {{0x8000000}}
Erase firmware from device:
st-flash erase
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
