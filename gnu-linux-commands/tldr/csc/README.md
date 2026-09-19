# csc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/csc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vue build
,
scrapy
,
miniserve
.
csc
The Microsoft C# Compiler.
More information:
https://docs.microsoft.com/dotnet/csharp/language-reference/compiler-options/command-line-building-with-csc-exe
.
Compile one or more C# files to a CIL executable:
csc {{path/to/input_file_a.cs}} {{path/to/input_file_b.cs}}
Specify the output filename:
csc /out:{{path/to/filename}} {{path/to/input_file.cs}}
Compile into a
.dll
library instead of an executable:
csc /target:library {{path/to/input_file.cs}}
Reference another assembly:
csc /reference:{{path/to/library.dll}} {{path/to/input_file.cs}}
Embed a resource:
csc /resource:{{path/to/resource_file}} {{path/to/input_file.cs}}
Automatically generate XML documentation:
csc /doc:{{path/to/output.xml}} {{path/to/input_file.cs}}
Specify an icon:
csc /win32icon:{{path/to/icon.ico}} {{path/to/input_file.cs}}
Strongly-name the resulting assembly with a keyfile:
csc /keyfile:{{path/to/keyfile}} {{path/to/input_file.cs}}
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
