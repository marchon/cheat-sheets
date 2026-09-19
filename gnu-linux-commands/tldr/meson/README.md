# meson

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/meson/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
borg
,
tee
,
phpstan
,
git whatchanged
.
meson
SCons-like build system that uses python as a front-end language and Ninja as a building backend.
More information:
https://mesonbuild.com
.
Generate a C project with a given name and version:
meson init --language={{c}} --name={{myproject}} --version={{0.1}}
Configure the
builddir
with default values:
meson setup {{build_dir}}
Build the project:
meson compile -C {{path/to/build_dir}}
Run all tests in the project:
meson test
Show the help:
meson --help
Show version info:
meson --version
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
