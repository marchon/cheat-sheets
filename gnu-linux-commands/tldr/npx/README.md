# npx

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/npx/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
seq
,
histexpand
,
[[
,
buzzphrase
.
npx
Execute binaries from
npm
packages.
More information:
https://github.com/npm/npx
.
Execute the binary from a given npm module:
npx {{module_name}} {{command_arguments}}
In case a package has multiple binaries, specify the package name along with the binary:
npx --package {{package_name}} {{module_name}}
Run a command if existis in the current path or in
node_modules/.bin
:
npx --no-install {{command}} {{command_arguments}}
Execute the binary from a given npm module suppressing any output from
npx
itself:
npx --quiet {{module_name}} {{command_arguments}}
Display help:
npx --help
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
