# ghdl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ghdl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ect
,
pio update
,
host
,
miniserve
.
ghdl
Open-source simulator for the VHDL language.
More information:
http://ghdl.free.fr
.
Analyze a VHDL source file and produce an object file:
ghdl -a {{filename.vhdl}}
Elaborate a design (where
{{design}}
is the name of a configuration unit, entity unit or architecture unit):
ghdl -e {{design}}
Run an elaborated design:
ghdl -r {{design}}
Run an elaborated design and dump output to a waveform file:
ghdl -r {{design}} --wave={{output.ghw}}
Check the syntax of a VHDL source file:
ghdl -s {{filename.vhdl}}
Display the help page:
ghdl --help
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
