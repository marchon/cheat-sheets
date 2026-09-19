# dotnet-tool

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dotnet-tool/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mongorestore
,
kotlin
,
lambo
,
virsh pool autostart
.
dotnet tool
Manage .NET tools and search published tools in NuGet.
More information:
https://docs.microsoft.com/dotnet/core/tools/global-tools
.
Install a global tool (don't use
--global
for local tools):
dotnet tool install --global {{dotnetsay}}
Install tools defined in the local tool manifest:
dotnet tool restore
Update a specific global tool (don't use
--global
for local tools):
dotnet tool update --global {{tool_name}}
Uninstall a global tool (don't use
--global
for local tools):
dotnet tool uninstall --global {{tool_name}}
List installed global tools (don't use
--global
for local tools):
dotnet tool list --global
Search tools in NuGet:
dotnet tool search {{search_term}}
Display help:
dotnet tool --help
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
