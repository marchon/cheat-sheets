# monodis

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/monodis/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
traceroute
,
git checkout index
.
monodis
The Mono Common Intermediate Language (CIL) disassembler.
More information:
https://www.mono-project.com/docs/tools+libraries/tools/monodis/
.
Disassemble an assembly to textual CIL:
monodis {{path/to/assembly.exe}}
Save the output to a file:
monodis --output={{path/to/output.il}} {{path/to/assembly.exe}}
Show information about an assembly:
monodis --assembly {{path/to/assembly.dll}}
List the references of an assembly:
monodis --assemblyref {{path/to/assembly.exe}}
List all the methods in an assembly:
monodis --method {{path/to/assembly.exe}}
Show a list of resources embedded within an assembly:
monodis --manifest {{path/to/assembly.dll}}
Extract all the embedded resources to the current directory:
monodis --mresources {{path/to/assembly.dll}}
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
