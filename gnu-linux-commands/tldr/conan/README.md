# conan

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/conan/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
trap
,
ember
,
pio platform
,
git svn
.
conan
The open source, decentralized and cross-platform package manager to create and share all your native binaries.
Some subcommands such as
conan frogarian
have their own usage documentation.
More information:
https://conan.io/
.
Install packages based on
conanfile.txt
:
conan install {{.}}
Install packages and create configuration files for a specific generator:
conan install -g {{generator}}
Install packages, building from source:
conan install {{.}} --build
Search for locally installed packages:
conan search {{package}}
Search for remote packages:
conan search {{package}} -r {{remote}}
List remotes:
conan remote list
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
