# go-vet

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/go-vet/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
carp
,
git graft
,
ulimit
,
cmatrix
.
go vet
Check Go source code and report suspicious constructs (e.g. lint your Go source files).
Go vet returns a non-zero exit code if problems are found; returns a zero exit code if no problems are found.
More information:
https://pkg.go.dev/cmd/vet
.
Check the Go package in the current directory:
go vet
Check the Go package in the specified path:
go vet {{path/to/file_or_directory}}
List available checks that can be run with go vet:
go tool vet help
View details and flags for a particular check:
go tool vet help {{check_name}}
Display offending lines plus N lines of surrounding context:
go vet -c={{N}}
Output analysis and errors in JSON format:
go vet -json
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
