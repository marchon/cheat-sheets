# iverilog

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/iverilog/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
speed test
,
pdfseparate
,
ss local
.
iverilog
Preprocesses and compiles Verilog HDL (IEEE-1364) code, into executable programs for simulation.
More information:
http://iverilog.icarus.com/
.
Compile a source file into an executable:
iverilog {{source.v}} -o {{executable}}
Also display all warnings:
iverilog {{source.v}} -Wall -o {{executable}}
Compile and run explicitly using the VVP runtime:
iverilog -o {{executable}} -tvvp {{source.v}}
Compile using Verilog library files from a different path:
iverilog {{source.v}} -o {{executable}} -I{{path/to/library_directory}}
Preprocess Verilog code without compiling:
iverilog -E {{source.v}}
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
