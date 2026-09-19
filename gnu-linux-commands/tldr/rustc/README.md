# rustc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rustc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
finger
,
multipass
,
git format patch
.
rustc
The Rust compiler.
Processes, compiles and links Rust language source files.
More information:
https://doc.rust-lang.org/rustc
.
Compile a single file:
rustc {{file.rs}}
Compile with high optimization:
rustc -O {{file.rs}}
Compile with debugging information:
rustc -g {{file.rs}}
Compile with architecture-specific optimizations for the current CPU:
rustc -C target-cpu=native {{path/to/file.rs}}
Display architecture-specific optimizations for the current CPU:
rustc -C target-cpu=native --print cfg
Display target list:
rustc --print target-list
Compile for a specific target:
rustc --target {{target_triple}} {{path/to/file.rs}}
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
