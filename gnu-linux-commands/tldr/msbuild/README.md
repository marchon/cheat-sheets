# msbuild

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/msbuild/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git mv
,
zig
,
gpg
,
7z
,
git subtree
.
msbuild
The Microsoft build tool for Visual Studio project solutions.
More information:
https://docs.microsoft.com/visualstudio/msbuild
.
Build the first project file in the current directory:
msbuild
Build a specific project file:
msbuild {{path/to/project_file}}
Set one or more semicolon-separated targets to build:
msbuild {{path/to/project_file}} /target:{{targets}}
Set one or more semicolon-separated properties:
msbuild {{path/to/project_file}} /property:{{name=value}}
Set the build tools version to use:
msbuild {{path/to/project_file}} /toolsversion:{{version}}
Display detailed information at the end of the log about how the project was configured:
msbuild {{path/to/project_file}} /detailedsummary
Display detailed help information:
msbuild /help
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
