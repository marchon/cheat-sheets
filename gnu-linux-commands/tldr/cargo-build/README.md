# cargo-build

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cargo-build/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dict
,
shasum
,
mycli
,
git ls remote
.
cargo build
Compile a local package and all of its dependencies.
More information:
https://doc.rust-lang.org/cargo/commands/cargo-build.html
.
Build the package or packages defined by the
Cargo.toml
manifest file in the local path:
cargo build
Build artifacts in release mode, with optimizations:
cargo build --release
Require that
Cargo.lock
is up to date:
cargo build --locked
Build all packages in the workspace:
cargo build --workspace
Build a specific package:
cargo build --package {{package}}
Build only the specified binary:
cargo build --bin {{name}}
Build only the specified test target:
cargo build --test {{testname}}
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
