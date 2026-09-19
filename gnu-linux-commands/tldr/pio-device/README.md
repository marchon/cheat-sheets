# pio-device

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pio-device/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
quilt
,
deluged
,
tmuxinator
,
tmux
.
pio device
Manage and monitor PlatformIO devices.
More information:
https://docs.platformio.org/en/latest/core/userguide/device/
.
List all available serial ports:
pio device list
List all available logical devices:
pio device list --logical
Start an interactive device monitor:
pio device monitor
Start an interactive device monitor and listen to a specific port:
pio device monitor --port {{/dev/ttyUSBX}}
Start an interactive device monitor and set a specific baud rate (defaults to 9600):
pio device monitor --baud {{57600}}
Start an interactive device monitor and set a specific EOL character (defaults to
CRLF
):
pio device monitor --eol {{CRLF|CR|LF}}
Go to the menu of the interactive device monitor:
Ctrl + T
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
