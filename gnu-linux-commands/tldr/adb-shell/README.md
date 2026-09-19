# adb-shell

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/adb-shell/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
doctl apps
,
timew
,
vcsh
,
wget
,
chezmoi
.
adb shell
Android Debug Bridge Shell: Run remote shell commands on an Android emulator instance or connected Android devices.
More information:
https://developer.android.com/studio/command-line/adb
.
Start a remote interactive shell on the emulator/device:
adb shell
Get all the properties from emulator or device:
adb shell getprop
Revert all runtime permissions to their default:
adb shell pm reset-permissions
Revoke a dangerous permission for an application:
adb shell pm revoke {{package}} {{permission}}
Trigger a key event:
adb shell input keyevent {{keycode}}
Clear the data of an application on an emulator or device:
adb shell pm clear {{package}}
Start an activity on emulator/device:
adb shell am start -n {{package}}/{{activity}}
Start the home activity on an emulator or device:
adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN
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
