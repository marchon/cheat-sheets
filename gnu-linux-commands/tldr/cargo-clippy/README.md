# cargo-clippy

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cargo-clippy/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
chroma
,
keybase
,
npm
,
go list
,
bvnc
.
cargo clippy
A collection of lints to catch common mistakes and improve your Rust code.
More information:
https://github.com/rust-lang/rust-clippy
.
Run checks over the code in the current directory:
cargo clippy
Require that
Cargo.lock
is up to date:
cargo clippy --locked
Run checks on all packages in the workspace:
cargo clippy --workspace
Run checks for a package:
cargo clippy --package {{package}}
Treat warnings as errors:
cargo clippy -- --deny warnings
Run checks and ignore warnings:
cargo clippy -- --allow warnings
Apply Clippy suggestions automatically:
cargo clippy --fix
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
