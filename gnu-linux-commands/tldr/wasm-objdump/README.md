# wasm-objdump

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/wasm-objdump/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pdftk
,
mcs
,
sha256sum
,
edgepaint
.
wasm-objdump
Display information from WebAssembly binaries.
More information:
https://github.com/WebAssembly/wabt
.
Display the section headers of a given binary:
wasm-objdump -h {{file.wasm}}
Display the entire disassembled output of a given binary:
wasm-objdump -d {{file.wasm}}
Display the details of each section:
wasm-objdump --details {{file.wasm}}
Display the details of a given section:
wasm-objdump --section '{{import}}' --details {{file.wasm}}
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
