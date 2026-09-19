# pnpm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pnpm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
quota
,
tlmgr paper
,
xml edit
.
pnpm
Fast, disk space efficient package manager for Node.js.
Manage Node.js projects and their module dependencies.
More information:
https://pnpm.io
.
Interactively create a
package.json
file:
pnpm init
Download all the packages listed as dependencies in
package.json
:
pnpm install
Download a specific version of a package and add it to the list of dependencies in
package.json
:
pnpm install {{module_name}}@{{version}}
Download a package and add it to the list of dev dependencies in
package.json
:
pnpm install --dev {{module_name}}
Download a package and install it globally:
pnpm install -g {{module_name}}
Uninstall a package and remove it from the list of dependencies in
package.json
:
pnpm uninstall {{module_name}}
Print a tree of locally installed modules:
pnpm list
List top-level [g]lobally installed modules:
pnpm list -g --depth={{0}}
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
