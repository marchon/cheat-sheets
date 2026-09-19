# cargo-rustc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cargo-rustc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xh
,
alex
,
az tag
,
pushd
,
serverless
.
cargo rustc
Compile a Rust package, and pass extra options to the compiler.
More information:
https://doc.rust-lang.org/cargo/commands/cargo-rustc.html
.
Build the package or packages defined by the
Cargo.toml
manifest file in the current working directory:
cargo rustc
Build artifacts in release mode, with optimizations:
cargo rustc --release
Compile with architecture-specific optimizations for the current CPU:
cargo rustc --release -- -C target-cpu=native
Compile with speed optimization:
cargo rustc -- -C opt-level {{1|2|3}}
Compile with [s]ize optimization (
z
also turns off loop vectorization):
cargo rustc -- -C opt-level {{s|z}}
Check if your package uses unsafe code:
cargo rustc --lib -- -D unsafe-code
Build a specific package:
cargo rustc --package {{package}}
Build only the specified binary:
cargo --bin {{name}}
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
