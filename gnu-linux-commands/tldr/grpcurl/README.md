# grpcurl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/grpcurl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
rdfind
,
glab issue
,
iex
,
pwsh
,
blackfire
.
grpcurl
Like cURL, but for gRPC: CLI tool for interacting with gRPC servers.
More information:
https://github.com/fullstorydev/grpcurl
.
Send an empty request:
grpcurl {{grpc.server.com:443}} {{my.custom.server.Service/Method}}
Send a request with a header and a body:
grpcurl -H "{{Authorization: Bearer $token}}" -d {{'{"foo": "bar"}'}} {{grpc.server.com:443}} {{my.custom.server.Service/Method}}
List all services exposed by a server:
grpcurl {{grpc.server.com:443}} list
List all methods in a particular service:
grpcurl {{grpc.server.com:443}} list {{my.custom.server.Service}}
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
