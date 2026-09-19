# go-test

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/go-test/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sfdp
,
docker run
,
rvm
,
amass enum
.
go test
Tests Go packages (files have to end with
_test.go
).
More information:
https://golang.org/cmd/go/#hdr-Testing_flags
.
Test the package found in the current directory:
go test
[v]erbosely test the package in the current directory:
go test -v
Test the packages in the current directory and all subdirectories (note the
...
):
go test -v ./...
Test the package in the current directory and run all benchmarks:
go test -v -bench .
Test the package in the current directory and run all benchmarks for 50 seconds:
go test -v -bench . -benchtime {{50s}}
Test the package with coverage analysis:
go test -cover
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
