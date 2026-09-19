# swc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/swc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
yt dlp
,
browser sync
,
pueue completions
.
swc
JavaScript and TypeScript compiler written in Rust.
More information:
https://swc.rs
.
Transpile a specified input file and output to stdout:
swc {{path/to/file}}
Transpile the input file every time it is changed:
swc {{path/to/file}} --watch
Transpile a specified input file and output to a specific file:
swc {{path/to/input_file}} --out-file {{path/to/output_file}}
Transpile a specified input directory and output to a specific directory:
swc {{path/to/input_directory}} --out-dir {{path/to/output_directory}}
Transpile a specified input directory using a specific configuration file:
swc {{path/to/input_directory}} --config-file {{path/to/.swcrc}}
Ignore files in a directory specified using glob path:
swc {{path/to/input_directory}} --ignore {{ignored_files}}
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
