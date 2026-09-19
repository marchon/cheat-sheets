# wapm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/wapm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virsh list
,
type
,
nmap
,
git add
.
wapm
The WebAssembly package manager.
More information:
https://wapm.io/help/reference
.
Interactively create a new
wapm.toml
file:
wapm init
Download all the packages listed as dependencies in
wapm.toml
:
wapm install
Download a specific version of a package and add it to the list of dependencies in wapm.toml:
wapm install {{package_name}}@{{version}}
Download a package and install it globally:
wapm install --global {{package_name}}
Uninstall a package and remove it from the list of dependencies in
wapm.toml
:
wapm uninstall {{package_name}}
Print a tree of locally installed dependencies:
wapm list
List top-level globally installed packages:
wapm list --global
Execute a package command using the Wasmer runtime:
wapm run {{command_name}} {{arguments}}
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
