# stl2gts

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/stl2gts/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
vimtutor
,
fastmod
,
comm
,
hexyl
.
stl2gts
Convert STL files into the GTS (GNU triangulated surface library) file format.
More information:
https://manned.org/stl2gts
.
Convert an STL file to a GTS file:
stl2gts < {{path/to/file.stl}} > {{path/to/file.gts}}
Convert an STL file to a GTS file and revert face normals:
stl2gts --revert < {{path/to/file.stl}} > {{path/to/file.gts}}
Convert an STL file to a GTS file and do not merge vertices:
stl2gts --nomerge < {{path/to/file.stl}} > {{path/to/file.gts}}
Convert an STL file to a GTS file and display surface statistics:
stl2gts --verbose < {{path/to/file.stl}} > {{path/to/file.gts}}
Print help for
stl2gts
:
stl2gts --help
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
