# npm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/npm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
musescore
,
lli
,
dvc freeze
,
screenfetch
.
npm
JavaScript and Node.js package manager.
Manage Node.js projects and their module dependencies.
More information:
https://www.npmjs.com
.
Interactively create a
package.json
file:
npm init
Download all the packages listed as dependencies in package.json:
npm install
Download a specific version of a package and add it to the list of dependencies in
package.json
:
npm install {{module_name}}@{{version}}
Download a package and add it to the list of dev dependencies in
package.json
:
npm install {{module_name}} --save-dev
Download a package and install it globally:
npm install --global {{module_name}}
Uninstall a package and remove it from the list of dependencies in
package.json
:
npm uninstall {{module_name}}
Print a tree of locally installed dependencies:
npm list
List top-level globally installed modules:
npm list --global --depth={{0}}
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
