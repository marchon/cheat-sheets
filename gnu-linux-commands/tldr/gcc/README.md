# gcc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gcc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
rcat
,
vue init
,
fgrep
,
nikto
,
date
.
gcc
Preprocess and compile C and C++ source files, then assemble and link them together.
More information:
https://gcc.gnu.org
.
Compile multiple source files into executable:
gcc {{path/to/source1.c path/to/source2.c ...}} --output {{path/to/output_executable}}
Allow warnings, debug symbols in output:
gcc {{path/to/source.c}} -Wall -Og --output {{path/to/output_executable}}
Include libraries from a different path:
gcc {{path/to/source.c}} --output {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}
Compile source code into Assembler instructions:
gcc -S {{path/to/source.c}}
Compile source code without linking:
gcc -c {{path/to/source.c}}
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
