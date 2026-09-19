# dotnet-restore

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dotnet-restore/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git lock
,
shopt
,
dhclient
,
home manager
.
dotnet restore
Restores the dependencies and tools of a .NET project.
More information:
https://docs.microsoft.com/dotnet/core/tools/dotnet-restore
.
Restore dependencies for a .NET project or solution in the current directory:
dotnet restore
Restore dependencies for a .NET project or solution in a specific location:
dotnet restore {{path/to/project_or_solution}}
Restore dependencies without caching the HTTP requests:
dotnet restore --no-cache
Force all dependencies to be resolved even if the last restore was successful:
dotnet restore --force
Restore dependencies using package source failures as warnings:
dotnet restore --ignore-failed-sources
Restore dependencies with a specific verbosity level:
dotnet restore --verbosity {{quiet|minimal|normal|detailed|diagnostic}}
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
