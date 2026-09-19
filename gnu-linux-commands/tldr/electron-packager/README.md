# electron-packager

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/electron-packager/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
wpscan
,
wapm
,
dvc freeze
,
xidel
.
electron-packager
A tool used to build Electron app executables for Windows, Linux and macOS.
Requires a valid package.json in the application directory.
More information:
https://github.com/electron/electron-packager
.
Package an application for the current architecture and platform:
electron-packager "{{path/to/app}}" "{{app_name}}"
Package an application for all architectures and platforms:
electron-packager "{{path/to/app}}" "{{app_name}}" --all
Package an application for 64-bit Linux:
electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{linux}}" --arch="{{x64}}"
Package an application for ARM macOS:
electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{darwin}}" --arch="{{arm64}}"
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
