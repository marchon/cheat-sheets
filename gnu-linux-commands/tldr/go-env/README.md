# go-env

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/go-env/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bosh
,
ssh keygen
,
cloc
,
ar
,
hakyll init
.
go env
Manage environment variables used by the Go toolchain.
More information:
https://golang.org/cmd/go/#hdr-Print_Go_environment_information
.
Show all environment variables:
go env
Show a specific environment variable:
go env {{GOPATH}}
Set an environment variable to a value:
go env -w {{GOBIN}}={{path/to/directory}}
Reset an environment variable's value:
go env -u {{GOBIN}}
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
