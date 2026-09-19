# go-build

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/go-build/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pdfjam
,
odps resource
,
gdrive
.
go build
Compile Go sources.
More information:
https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies
.
Compile a 'package main' file (output will be the filename without extension):
go build {{path/to/main.go}}
Compile, specifying the output filename:
go build -o {{path/to/binary}} {{path/to/source.go}}
Compile a package:
go build -o {{path/to/binary}} {{path/to/package}}
Compile a main package into an executable, enabling data race detection:
go build -race -o {{path/to/executable}} {{path/to/main/package}}
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
