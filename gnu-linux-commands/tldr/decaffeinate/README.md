# decaffeinate

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/decaffeinate/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pkill
,
snyk
,
man
,
wrangler
,
phploc
.
decaffeinate
Move your CoffeeScript source to modern JavaScript.
More information:
https://decaffeinate-project.org
.
Convert a CoffeeScript file to JavaScript:
decaffeinate {{path/to/file.coffee}}
Convert a CoffeeScript v2 file to JavaScript:
decaffeinate --use-cs2 {{path/to/file.coffee}}
Convert require and
module.exports
to import and export:
decaffeinate --use-js-modules {{path/to/file.coffee}}
Convert a CoffeeScript, allowing named exports:
decaffeinate --loose-js-modules {{path/to/file.coffee}}
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
