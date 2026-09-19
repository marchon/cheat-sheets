# qdbus

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/qdbus/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
grpcurl
,
rtv
,
gnucash
,
git missing
.
qdbus
Inter-Process Communication (IPC) and Remote Procedure Calling (RPC) mechanism originally developed for Linux.
More information:
https://doc.qt.io/qt-5/qtdbus-index.html
.
List available service names:
qdbus
List object paths for a specific service:
qdbus {{service_name}}
List methods, signals and properties available on a specific object:
qdbus {{service_name}} {{/path/to/object}}
Execute a specific method passing arguments and display the returned value:
qdbus {{service_name}} {{/path/to/object}} {{method_name}} {{argument1}} {{argument2}}
Display the current brightness value in a KDE Plasma session:
qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness}}
Set a specific brightness to a KDE Plasma session:
qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness}} {{5000}}
Invoke volume up shortcut in a KDE Plasma session:
qdbus {{org.kde.kglobalaccel}} {{/component/kmix}} {{invokeShortcut}} "{{increase_volume}}"
Display help:
qdbus --help
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
