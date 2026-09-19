# meshlabserver

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/meshlabserver/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
packtpub
,
jello
,
kak
,
swagger codegen
.
meshlabserver
Command-line interface for the MeshLab 3D mesh processing software.
More information:
https://manned.org/meshlabserver
.
Convert an STL file to an OBJ file:
meshlabserver -i {{input.stl}} -o {{output.obj}}
Convert a WRL file to a OFF file, including the vertex and face normals in the output mesh:
meshlabserver -i {{input.wrl}} -o {{output.off}} -om vn fn
Dump a list of all the available processing filters into a file:
meshlabserver -d {{filename}}
Process a 3D file using a filter script created in the MeshLab GUI (Filters > Show current filter script > Save Script):
meshlabserver -i {{input.ply}} -o {{output.ply}} -s {{filter_script.mlx}}
Process a 3D file using a filter script, writing the output of the filters into a log file:
meshlabserver -i {{input.x3d}} -o {{output.x3d}} -s {{filter_script.mlx}} -l {{logfile}}
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
