# go-tool

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/go-tool/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
export
,
zstd
,
git extras
,
gibo
.
go tool
Run a specific Go tool or command.
Execute a Go command as a stand-alone binary, typically for debugging.
More information:
https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool
.
List available tools:
go tool
Run the go link tool:
go tool link {{path/to/main.o}}
Print the command that would be executed, but do not execute it (similar to
whereis
):
go tool -n {{command}} {{arguments}}
Display documentation for a specified tool:
go tool {{command}} --help
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
