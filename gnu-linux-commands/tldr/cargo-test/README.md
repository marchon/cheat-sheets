# cargo-test

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cargo-test/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git lock
,
svgcleaner
,
hg status
.
cargo test
Execute the unit and integration tests of a Rust package.
More information:
https://doc.rust-lang.org/cargo/commands/cargo-test.html
.
Only run tests containing a specific string in their names:
cargo test {{testname}}
Set the number of simultaneous running test cases:
cargo test -- --test-threads={{count}}
Require that
Cargo.lock
is up to date:
cargo test --locked
Test artifacts in release mode, with optimizations:
cargo test --release
Test all packages in the workspace:
cargo test --workspace
Run tests for a package:
cargo test --package {{package}}
Run tests without hiding output from test executions:
cargo test -- --nocapture
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
