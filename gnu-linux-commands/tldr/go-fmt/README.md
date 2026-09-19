# go-fmt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/go-fmt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
iconv
,
virsh pool define as
.
go fmt
Format Go source files.
Prints the filenames that are changed.
More information:
https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources
.
Format Go source files in the current directory:
go fmt
Format a specific Go package in your import path (
$GOPATH/src
):
go fmt {{path/to/package}}
Format the package in the current directory and all subdirectories (note the
...
):
go fmt {{./...}}
Print what format commands would've been run, without modifying anything:
go fmt -n
Print which format commands are run as they are run:
go fmt -x
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
