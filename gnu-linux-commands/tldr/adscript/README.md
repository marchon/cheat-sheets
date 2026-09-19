# adscript

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/adscript/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fc list
,
betty
,
guetzli
,
objdump
.
adscript
Compiler for Adscript files.
More information:
https://github.com/Amplus2/Adscript
.
Compile a file to an object file:
adscript --output {{path/to/file.o}} {{path/to/input_file.adscript}}
Compile and link a file to a standalone executable:
adscript --executable --output {{path/to/file}} {{path/to/input_file.adscript}}
Compile a file to LLVM IR instead of native machine code:
adscript --llvm-ir --output {{path/to/file.ll}} {{path/to/input_file.adscript}}
Cross-compile a file to an object file for a foreign CPU architecture or operating system:
adscript --target-triple {{i386-linux-elf}} --output {{path/to/file.o}} {{path/to/input_file.adscript}}
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
