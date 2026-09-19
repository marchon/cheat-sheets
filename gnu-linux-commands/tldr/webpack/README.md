# webpack

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/webpack/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mocha
,
git ignore io
,
heroku
.
webpack
Bundle a web project's js files and other assets into a single output file.
More information:
https://webpack.js.org
.
Create a single output file from an entry point file:
webpack {{app.js}} {{bundle.js}}
Load CSS files too from the JavaScript file (this uses the CSS loader for
.css
files):
webpack {{app.js}} {{bundle.js}} --module-bind '{{css=css}}'
Pass a config file (with e.g. the entry script and the output filename) and show compilation progress:
webpack --config {{webpack.config.js}} --progress
Automatically recompile on changes to project files:
webpack --watch {{app.js}} {{bundle.js}}
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
