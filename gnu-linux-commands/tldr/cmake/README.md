# cmake

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cmake/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
searchsploit
,
kill
,
autojump
.
cmake
Cross-platform build automation system, that generates recipes for native build systems.
More information:
https://cmake.org/cmake/help/latest/manual/cmake.1.html
.
Generate a build recipe in the current directory with
CMakeLists.txt
from a project directory:
cmake {{path/to/project_directory}}
Generate a build recipe, with build type set to
Release
with CMake variable:
cmake {{path/to/project_directory}} -D {{CMAKE_BUILD_TYPE=Release}}
Use a generated recipe in a given directory to build artifacts:
cmake --build {{path/to/build_directory}}
Install the build artifacts into
/usr/local/
and strip debugging symbols:
cmake --install {{path/to/build_directory}} --strip
Install the build artifacts using the custom prefix for paths:
cmake --install {{path/to/build_directory}} --strip --prefix {{path/to/directory}}
Run a custom build target:
cmake --build {{path/to/build_directory}} --target {{target_name}}
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
