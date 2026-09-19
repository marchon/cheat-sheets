# kitex

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/kitex/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pvecm
,
grex
,
dict
,
test
,
unlink
,
tlmgr candidates
.
kitex
Code generation tool provided by the Go RPC framework Kitex.
Kitex accepts both thrift and protobuf IDLs, and supports generating a skeleton of a server side project.
More information:
https://www.cloudwego.io
.
Generate client codes when a project is in
$GOPATH
:
kitex {{path/to/IDL_file.thrift}}
Generate client codes when a project is not in
$GOPATH
:
kitex -module {{github.com/xx-org/xx-name}} {{path/to/IDL_file.thrift}}
Generate client codes with protobuf IDL:
kitex -type protobuf {{path/to/IDL_file.proto}}
Generate server codes:
kitex -service {{svc_name}} {{path/to/IDL_file.thrift}}
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
