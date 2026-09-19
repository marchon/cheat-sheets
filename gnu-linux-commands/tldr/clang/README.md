# clang

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/clang/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
aws ecr
,
rails db
,
uptime
,
pipenv
.
clang
Compiler for C, C++, and Objective-C source files. Can be used as a drop-in replacement for GCC.
More information:
https://clang.llvm.org/docs/ClangCommandLineReference.html
.
Compile a source code file into an executable binary:
clang {{input_source.c}} -o {{output_executable}}
Activate output of all errors and warnings:
clang {{input_source.c}} -Wall -o {{output_executable}}
Include libraries located at a different path than the source file:
clang {{input_source.c}} -o {{output_executable}} -I{{header_path}} -L{{library_path}} -l{{library_name}}
Compile source code into LLVM Intermediate Representation (IR):
clang -S -emit-llvm {{file.c}} -o {{file.ll}}
Compile source code without linking:
clang -c {{input_source.c}}
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
