# pio-ci

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pio-ci/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fselect
,
php yii
,
django admin
.
pio ci
Build PlatformIO projects with an arbitrary source code structure.
This will create a new temporary project which the source code will be copied into.
More information:
https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html
.
Build a PlatformIO project in the default system temporary directory and delete it afterwards:
pio ci {{path/to/project}}
Build a PlatformIO project and specify specific libraries:
pio ci --lib {{path/to/library_directory}} {{path/to/project}}
Build a PlatformIO project and specify a specific board (
pio boards
lists all of them):
pio ci --board {{board}} {{path/to/project}}
Build a PlatformIO project in a specific directory:
pio ci --build-dir {{path/to/build_directory}} {{path/to/project}}
Build a PlatformIO project and don't delete the build directory:
pio ci --keep-build-dir {{path/to/project}}
Build a PlatformIO project using a specific configuration file:
pio ci --project-conf {{path/to/platformio.ini}}
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
