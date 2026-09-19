# xxd

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xxd/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pdfseparate
,
csc
,
swift
,
pkill
.
xxd
Create a hexadecimal representation (hexdump) from a binary file, or vice-versa.
More information:
https://manned.org/xxd
.
Generate a hexdump from a binary file and display the output:
xxd {{input_file}}
Generate a hexdump from a binary file and save it as a text file:
xxd {{input_file}} {{output_file}}
Display a more compact output, replacing consecutive zeros (if any) with a star:
xxd -a {{input_file}}
Display the output with 10 columns of one octet (byte) each:
xxd -c {{10}} {{input_file}}
Display output only up to a length of 32 bytes:
xxd -l {{32}} {{input_file}}
Display the output in plain mode, without any gaps between the columns:
xxd -p {{input_file}}
Revert a plaintext hexdump back into binary, and save it as a binary file:
xxd -r -p {{input_file}} {{output_file}}
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
