# swig

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/swig/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git create branch
,
hyperfine
.
swig
Generate bindings between C / C++ code and various high level languages such as JavaScript, Python, C#, and more.
It uses special .i or .swg files to generate the bindings (C/C++ with SWIG directives, then outputs a C/C++ file that contains all the wrapper code needed to build an extension module.
More information:
http://www.swig.org
.
Generate a binding between C++ and Python:
swig -c++ -python -o {{path/to/output_wrapper.cpp}} {{path/to/swig_file.i}}
Generate a binding between C++ and Go:
swig -go -cgo -intgosize 64 -c++ {{path/to/swig_file.i}}
Generate a binding between C and Java:
swig -java {{path/to/swig_file.i}}
Generate a binding between C and Ruby and prefix the Ruby module with {{foo::bar::}}:
swig -ruby -prefix "{{foo::bar::}}" {{path/to/swig_file.i}}
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
