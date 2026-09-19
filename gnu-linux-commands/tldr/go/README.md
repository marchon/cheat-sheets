# go

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/go/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vue
,
sdkmanager
,
pio debug
,
sort
.
go
Tool for managing go source code.
Some subcommands such as
go build
have their own usage documentation.
More information:
https://golang.org
.
Download and install a package, specified by its import path:
go get {{package_path}}
Compile and run a source file (it has to contain a
main
package):
go run {{file}}.go
Compile a source file into a named executable:
go build -o {{executable}} {{file}}.go
Compile the package present in the current directory:
go build
Execute all test cases of the current package (files have to end with
_test.go
):
go test
Compile and install the current package:
go install
Initialize a new module in the current directory:
go mod init {{module_name}}
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
