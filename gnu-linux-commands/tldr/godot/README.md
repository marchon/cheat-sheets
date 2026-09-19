# godot

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/godot/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ts
,
dolt branch
,
tig
,
task
,
httping
.
godot
An open source 2D and 3D game engine.
More information:
https://godotengine.org/
.
Run a project if the current directory contains a
project.godot
file, otherwise open the project manager:
godot
Edit a project (the current directory must contain a
project.godot
file):
godot -e
Open the project manager even if the current directory contains a
project.godot
file:
godot -p
Export a project for a given export preset (the preset must be defined in the project):
godot --export {{preset}} {{output_path}}
Execute a standalone GDScript file (the script must inherit from
SceneTree
or
MainLoop
):
godot -s {{script.gd}}
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
