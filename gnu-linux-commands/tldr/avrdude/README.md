# avrdude

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/avrdude/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
erl
,
file
,
msmtp
,
umount
,
apktool
.
avrdude
Driver program for Atmel AVR microcontrollers programming.
More information:
https://www.nongnu.org/avrdude/
.
Read AVR microcontroller:
avrdude -p {{AVR_device}} -c {{programmer}} -U flash:r:{{file.hex}}:i
Write AVR microcontroller:
avrdude -p {{AVR_device}} -c {{programmer}} -U flash:w:{{file.hex}}
List available AVR devices:
avrdude -p \?
List available AVR programmers:
avrdude -c \?
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
