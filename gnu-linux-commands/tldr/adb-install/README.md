# adb-install

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/adb-install/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vagrant
,
zek
,
axel
,
qr
,
telnet
,
rev
.
adb install
Android Debug Bridge Install: Push packages to an Android emulator instance or connected Android devices.
More information:
https://developer.android.com/studio/command-line/adb
.
Push an Android application to an emulator/device:
adb install {{path/to/file.apk}}
Push an Android application to a specific emulator/device (overrides
$ANDROID_SERIAL
):
adb -s {{serial_number}} install {{path/to/file.apk}}
Reinstall an existing app, keeping its data:
adb install -r {{path/to/file.apk}}
Grant all permissions listed in the app manifest:
adb install -g {{path/to/file.apk}}
Quickly update an installed package by only updating the parts of the APK that changed:
adb install --fastdeploy {{path/to/file.apk}}
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
