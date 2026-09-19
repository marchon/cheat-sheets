# st-util

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/st-util/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aws lambda
,
perl
,
phpstorm
,
smartctl
.
st-util
Run GDB (GNU Debugger) server to interact with STM32 ARM Cortex microcontoller.
More information:
https://github.com/texane/stlink
.
Run GDB server on port 4500:
st-util -p {{4500}}
Connect to GDB server:
(gdb) target extended-remote {{localhost}}:{{4500}}
Write firmware to device:
(gdb) load {{firmware.elf}}
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
