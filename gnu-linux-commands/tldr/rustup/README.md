# rustup

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rustup/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fusermount
,
xml edit
,
z
,
awslogs
.
rustup
Rust toolchain installer.
Install, manage, and update Rust toolchains.
More information:
https://github.com/rust-lang/rustup.rs
.
Install the nightly toolchain for your system:
rustup install nightly
Switch the default toolchain to nightly so that the
cargo
and
rustc
commands will use it:
rustup default nightly
Use the nightly toolchain when inside the current project, but leave global settings unchanged:
rustup override set nightly
Update all toolchains:
rustup update
List installed toolchains:
rustup show
Run cargo build with a certain toolchain:
rustup run {{toolchain_name}} cargo build
Open the local rust documentation in the default web browser:
rustup doc
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
