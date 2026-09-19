# b2sum

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/b2sum/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fzf
,
glab issue
,
lynx
,
drupal check
.
b2sum
Calculate BLAKE2 cryptographic checksums.
More information:
https://www.gnu.org/software/coreutils/b2sum
.
Calculate the BLAKE2 checksum for a file:
b2sum {{path/to/file}}
Calculate BLAKE2 checksums for multiple files:
b2sum {{path/to/file1}} {{path/to/file2}}
Calculate the BLAKE2 checksum from stdin:
{{some_command}} | b2sum
Read a file of BLAKE2 sums and filenames and verify all files have matching checksums:
b2sum --check {{path/to/file.b2}}
Only show a message for missing files or when verification fails:
b2sum --check --quiet {{path/to/file.b2}}
Only show a message for files for which verification fails, ignoring missing files:
b2sum --ignore-missing --check --quiet {{path/to/file.b2}}
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
