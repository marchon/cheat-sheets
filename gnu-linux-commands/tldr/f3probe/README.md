# f3probe

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/f3probe/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
local
,
autojump
,
nop
,
pwd
,
basename
.
f3probe
Probe a block device (e.g. a flash drive or a microSD card) for counterfeit flash memory.
See also
f3read
,
f3write
,
f3fix
.
More information:
https://github.com/AltraMayor/f3
.
Probe a block device:
sudo f3probe {{path/to/block_device}}
Use the minimum about of RAM possible:
sudo f3probe --min-memory {{path/to/block_device}}
Time disk operations:
sudo f3probe --time-ops {{path/to/block_device}}
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
