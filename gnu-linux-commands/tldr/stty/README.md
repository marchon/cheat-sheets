# stty

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/stty/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
strings
,
ffsend
,
openssl s_client
.
stty
Set options for a terminal device interface.
More information:
https://www.gnu.org/software/coreutils/stty
.
Display all settings for the current terminal:
stty -a
Set the number of rows:
stty rows {{rows}}
Set the number of columns:
stty cols {{cols}}
Get the actual transfer speed of a device:
stty -F {{path/to/device_file}} speed
Reset all modes to reasonable values for the current terminal:
stty sane
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
