# fastboot

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/fastboot/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mkfifo
,
aws ses
,
sendmail
,
nl
,
atoum
.
fastboot
Communicate with connected Android devices when in bootloader mode (the one place
adb
doesn't work).
More information:
https://cs.android.com/android/platform/superproject/+/master:system/core/fastboot
.
Unlock the bootloader:
fastboot oem unlock
Relock the bootloader:
fastboot oem lock
Reboot the device from fastboot mode into fastboot mode again:
fastboot reboot bootloader
Flash a given image:
fastboot flash {{file.img}}
Flash a custom recovery image:
fastboot flash recovery {{file.img}}
Display connected devices:
fastboot devices
Display all information of a device:
fastboot getvar all
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
