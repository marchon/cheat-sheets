# nodemon

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nodemon/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az pipelines
,
autoflake
,
cargo rustc
.
nodemon
Watch files and automatically restart a node application when changes are detected.
More information:
https://nodemon.io
.
Execute the specified file and watch a specific file for changes:
nodemon {{path/to/file.js}}
Manually restart nodemon (note nodemon must already be active for this to work):
rs
Ignore specific files:
nodemon --ignore {{path/to/file_or_directory}}
Pass arguments to the node application:
nodemon {{path/to/file.js}} {{arguments}}
Pass arguments to node itself if they're not nodemon arguments already (e.g.
--inspect
):
nodemon {{arguments}} {{path/to/file.js}}
Run an arbitrary non-node script:
nodemon --exec "{{command_to_run_script}} {{options}}" {{path/to/script}}
Run a Python script:
nodemon --exec "python {{options}}" {{path/to/file.py}}
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
