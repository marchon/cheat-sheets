# arduino-builder

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/arduino-builder/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xml validate
,
csvcut
,
box
,
phive
.
arduino-builder
A command-line tool for compiling arduino sketches.
DEPRECATION WARNING: This tool is being phased out in favor of
arduino
.
More information:
https://github.com/arduino/arduino-builder
.
Compile a sketch:
arduino-builder -compile {{path/to/sketch.ino}}
Specify the debug level (1 to 10, defaults to 5):
arduino-builder -debug-level {{level}}
Specify a custom build directory:
arduino-builder -build-path {{path/to/build_directory}}
Use a build option file, instead of specifying
--hardware
,
--tools
, etc. manually every time:
arduino-builder -build-options-file {{path/to/build.options.json}}
Enable verbose mode:
arduino-builder -verbose {{true}}
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
