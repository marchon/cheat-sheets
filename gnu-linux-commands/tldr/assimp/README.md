# assimp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/assimp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
makensis
,
groups
,
numfmt
,
virsh pool list
.
assimp
Command-line client for the Open Asset Import Library.
Supports loading of 40+ 3D file formats, and exporting to several popular 3D formats.
More information:
http://www.assimp.org/
.
List all supported import formats:
assimp listext
List all supported export formats:
assimp listexport
Convert a file to one of the supported output formats, using the default parameters:
assimp export {{input_file.stl}} {{output_file.obj}}
Convert a file using custom parameters (the dox_cmd.h file in assimp's source code lists available parameters):
assimp export {{input_file.stl}} {{output_file.obj}} {{parameters}}
Display a summary of a 3D file's contents:
assimp info {{path/to/file}}
List all supported subcommands ("verbs"):
assimp help
Get help on a specific subcommand (e.g. the parameters specific to it):
assimp {{subcommand}} --help
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
