# browser-sync

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/browser-sync/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aws iam
,
ack
,
wuzz
,
decaffeinate
.
browser-sync
Starts local web server that updates browser on file changes.
More information:
https://browsersync.io/docs/command-line
.
Start a server from a specific directory:
browser-sync start --server {{path/to/directory}} --files {{path/to/directory}}
Start a server from local directory, watching all CSS files in a directory:
browser-sync start --server --files '{{path/to/directory/*.css}}'
Create configuration file:
browser-sync init
Start browser-sync from config file:
browser-sync start --config {{config_file}}
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
