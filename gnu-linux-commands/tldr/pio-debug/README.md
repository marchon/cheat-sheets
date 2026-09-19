# pio-debug

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pio-debug/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git fetch
,
starship
,
less
,
tr
,
openssl req
.
pio debug
Debug PlatformIO projects.
More information:
https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html
.
Debug the PlatformIO project in the current directory:
pio debug
Debug a specific PlatformIO project:
pio debug --project-dir {{path/to/platformio_project}}
Debug a specific environment:
pio debug --environment {{environment}}
Debug a PlatformIO project using a specific configuration file:
pio debug --project-conf {{path/to/platformio.ini}}
Debug a PlatformIO project using the
gdb
debugger:
pio debug --interface={{gdb}} {{gdb_options}}
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
