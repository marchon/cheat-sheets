# bower

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bower/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
lpstat
,
git format patch
,
mongo
.
bower
A package manager optimized for front-end web development.
A package can be a GitHub user/repo shorthand, a Git endpoint, a URL or a registered package.
More information:
https://bower.io/
.
Install a project's dependencies, listed in its bower.json:
bower install
Install one or more packages to the bower_components directory:
bower install {{package}} {{package}}
Uninstall packages locally from the bower_components directory:
bower uninstall {{package}} {{package}}
List local packages and possible updates:
bower list
Display help information about a bower command:
bower help {{command}}
Create a
bower.json
file for your package:
bower init
Install a specific dependency version, and add it to
bower.json
:
bower install {{local_name}}={{package}}#{{version}} --save
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
