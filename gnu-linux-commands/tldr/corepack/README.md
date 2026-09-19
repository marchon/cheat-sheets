# corepack

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/corepack/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
radare2
,
kube capacity
,
arp scan
.
corepack
Zero-runtime-dependency package acting as bridge between Node projects and their package managers.
More information:
https://github.com/nodejs/corepack
.
Add the Corepack shims to the Node.js installation directory to make them available as global commands:
corepack enable
Add the Corepack shims to a specific directory:
corepack enable --install-directory {{path/to/directory}}
Remove the Corepack shims from the Node.js installation directory:
corepack disable
Prepare a specific package manager:
corepack prepare {{package_manager}}@{{version}} --activate
Prepare the package manager configured for the project in the current path:
corepack prepare
Use a package manager without installing it as a global command:
corepack {{npm|pnpm|yarn}} {{package_manager_arguments}}
Install a package manager from the specified archive:
corepack hydrate {{path/to/corepack.tgz}}
Display help for a subcommand:
corepack {{subcommand}} --help
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
