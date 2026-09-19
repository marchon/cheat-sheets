# ld

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ld/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bindkey
,
jenv
,
u3d
,
virsh pool destroy
.
ld
Link object files together.
More information:
https://sourceware.org/binutils/docs-2.38/ld.html
.
Link a specific object file with no dependencies into an executable:
ld {{path/to/file.o}} --output {{path/to/output_executable}}
Link two object files together:
ld {{path/to/file1.o}} {{path/to/file2.o}} --output {{path/to/output_executable}}
Dynamically link an x86_64 program to glibc (file paths change depending on the system):
ld --output {{path/to/output_executable}} --dynamic-linker /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{path/to/file.o}} /lib/crtn.o
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
