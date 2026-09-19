# monop

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/monop/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
plesk
,
yank
,
tlmgr option
,
ipython
.
monop
Finds and displays signatures of Types and methods inside .NET assemblies.
More information:
https://manned.org/monop
.
Show the structure of a Type built-in of the .NET Framework:
monop {{System.String}}
List the types in an assembly:
monop -r:{{path/to/assembly.exe}}
Show the structure of a Type in a specific assembly:
monop -r:{{path/to/assembly.dll}} {{Namespace.Path.To.Type}}
Only show members defined in the specified Type:
monop -r:{{path/to/assembly.dll}} --only-declared {{Namespace.Path.To.Type}}
Show private members:
monop -r:{{path/to/assembly.dll}} --private {{Namespace.Path.To.Type}}
Hide obsolete members:
monop -r:{{path/to/assembly.dll}} --filter-obsolete {{Namespace.Path.To.Type}}
List the other assemblies that a specified assembly references:
monop -r:{{path/to/assembly.dll}} --refs
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
