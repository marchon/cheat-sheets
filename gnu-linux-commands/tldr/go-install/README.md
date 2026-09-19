# go-install

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/go-install/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git show
,
nodenv
,
lein
,
dog
,
ffmpeg
.
go install
Compile and install packages named by the import paths.
More information:
https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies
.
Compile and install the current package:
go install
Compile and install a specific local package:
go install {{path/to/package}}
Install the latest version of a program, ignoring
go.mod
in the current directory:
go install {{golang.org/x/tools/gopls}}@{{latest}}
Install a program at the version selected by
go.mod
in the current directory:
go install {{golang.org/x/tools/gopls}}
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
