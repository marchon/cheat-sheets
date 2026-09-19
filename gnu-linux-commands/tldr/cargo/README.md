# cargo

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cargo/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
csvgrep
,
isisdl
,
chromium
,
mpg321
.
cargo
Manage Rust projects and their module dependencies (crates).
Some subcommands such as
cargo build
have their own usage documentation.
More information:
https://crates.io/
.
Search for crates:
cargo search {{search_string}}
Install a crate:
cargo install {{crate_name}}
List installed crates:
cargo install --list
Create a new binary or library Rust project in the current directory:
cargo init --{{bin|lib}}
Create a new binary or library Rust project in the specified directory:
cargo new {{path/to/directory}} --{{bin|lib}}
Build the Rust project in the current directory:
cargo build
Build using a specific number of threads (default is the number of CPU cores):
cargo build --jobs {{number_of_threads}}
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
