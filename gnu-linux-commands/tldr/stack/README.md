# stack

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/stack/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ts
,
pveperf
,
stack
,
sfdp
,
virt sparsify
.
stack
Tool for managing Haskell projects.
More information:
https://github.com/commercialhaskell/stack
.
Create a new package:
stack new {{package_name}} {{template_name}}
Compile a package:
stack build
Run tests inside a package:
stack test
Compile a project and re-compile every time a file changes:
stack build --file-watch
Compile a project and execute a command after compilation:
stack build --exec "{{command}}"
Run a program and pass an argument to it:
stack exec {{program_name}} -- {{argument}}
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
