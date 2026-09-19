# arduino

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/arduino/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
steamcmd
,
qpdf
,
vagrant
,
rabin2
.
arduino
Arduino Studio - Integrated Development Environment for the Arduino platform.
More information:
https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc
.
Build a sketch:
arduino --verify {{path/to/file.ino}}
Build and upload a sketch:
arduino --upload {{path/to/file.ino}}
Build and upload a sketch to an Arduino Nano with an Atmega328p CPU, connected on port
/dev/ttyACM0
:
arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{path/to/file.ino}}
Set the preference
name
to a given
value
:
arduino --pref {{name}}={{value}}
Build a sketch, put the build results in the build directory, and reuse any previous build results in that directory:
arduino --pref build.path={{path/to/build_directory}} --verify {{path/to/file.ino}}
Save any (changed) preferences to
preferences.txt
:
arduino --save-prefs
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
