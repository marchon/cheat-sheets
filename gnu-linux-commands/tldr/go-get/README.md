# go-get

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/go-get/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git bisect
,
slimrb
,
cotton
,
killall
.
go get
Add a dependency package, or download packages in legacy GOPATH mode.
More information:
https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them
.
Add a specified package to
go.mod
in module-mode or install the package in GOPATH-mode:
go get {{example.com/pkg}}
Modify the package with a given version in module-aware mode:
go get {{example.com/pkg}}@{{v1.2.3}}
Remove a specified package:
go get {{example.com/pkg}}@{{none}}
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
