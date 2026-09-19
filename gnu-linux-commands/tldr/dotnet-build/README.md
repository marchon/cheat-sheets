# dotnet-build

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dotnet-build/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virsh undefine
,
eget
,
git commit
.
dotnet build
Builds a .NET application and its dependencies.
More information:
https://docs.microsoft.com/dotnet/core/tools/dotnet-build
.
Compile the project or solution in the current directory:
dotnet build
Compile a .NET project or solution in debug mode:
dotnet build {{path/to/project_or_solution}}
Compile in release mode:
dotnet build --configuration {{Release}}
Compile without restoring dependencies:
dotnet build --no-restore
Compile with a specific verbosity level:
dotnet build --verbosity {{quiet|minimal|normal|detailed|diagnostic}}
Compile for a specific runtime:
dotnet build --runtime {{runtime_identifier}}
Specify the output directory:
dotnet build --output {{path/to/directory}}
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
