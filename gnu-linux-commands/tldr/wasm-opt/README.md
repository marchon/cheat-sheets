# wasm-opt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/wasm-opt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ag
,
csc
,
gh issue create
,
deluge
.
wasm-opt
Optimize WebAssembly binary files.
More information:
https://github.com/webassembly/binaryen
.
Apply default optimizations and write to a given file:
wasm-opt -O {{input.wasm}} -o {{output.wasm}}
Apply all optimizations and write to a given file (takes more time, but generates optimal code):
wasm-opt -O4 {{input.wasm}} -o {{output.wasm}}
Optimize a file for size:
wasm-opt -Oz {{input.wasm}} -o {{output.wasm}}
Print the textual representation of the binary to console:
wasm-opt {{input.wasm}} --print
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
