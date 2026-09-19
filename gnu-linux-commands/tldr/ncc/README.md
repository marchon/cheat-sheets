# ncc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ncc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bundletool validate
,
dumpcap
.
ncc
Compile a Node.js application into a single file.
Supports TypeScript, binary addons and dynamic requires.
More information:
https://github.com/vercel/ncc
.
Bundle a Node.js application:
ncc build {{path/to/file.js}}
Bundle and minify a Node.js application:
ncc build --minify {{path/to/file.js}}
Bundle and minify a Node.js application and generate source maps:
ncc build --source-map {{path/to/file.js}}
Automatically recompile on changes to source files:
ncc build --watch {{path/to/file.js}}
Bundle a Node.js application into a temporary directory and run it for testing:
ncc run {{path/to/file.js}}
Clean the
ncc
cache:
ncc clean cache
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
