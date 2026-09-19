# scrcpy

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/scrcpy/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
croc
,
go generate
,
sccmap
,
lt
,
scrapy
.
scrcpy
Display and control your Android device on a desktop.
More information:
https://github.com/Genymobile/scrcpy
.
Display a mirror of a connected device:
scrcpy
Display a mirror of a specific device based on its ID or IP address (find it under the
adb devices
command):
scrcpy --serial {{0123456789abcdef|192.168.0.1:5555}}
Start display in fullscreen mode:
scrcpy --fullscreen
Rotate the display screen. Each incremental value adds a 90 degree counterclockwise rotation:
scrcpy --rotation {{0|1|2|3}}
Show touches on physical device:
scrcpy --show-touches
Record display screen:
scrcpy --record {{path/to/file.mp4}}
Set target directory for pushing files to device by drag and drop (non-APK):
scrcpy --push-target {{path/to/directory}}
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
