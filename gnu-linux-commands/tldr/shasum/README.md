# shasum

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/shasum/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh alias
,
tldr lint
,
find
,
pgrep
.
shasum
Calculate or check cryptographic SHA checksums.
More information:
https://manned.org/shasum
.
Calculate the SHA1 checksum for a file:
shasum {{path/to/file}}
Calculate the SHA256 checksum for a file:
shasum --algorithm 256 {{path/to/file}}
Calculate the SHA512 checksum for multiple files:
shasum --algorithm 512 {{path/to/file1}} {{path/to/file2}}
Calculate and save the list of SHA256 checksums to a file:
shasum --algorithm 256 {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha256}}
Check a file with a list of sums against the directory's files:
shasum --check {{path/to/file}}
Check a list of sums and only show a message for files for which verification fails:
shasum --check --quiet {{path/to/file}}
Calculate the SHA1 checksum from stdin:
{{some_command}} | shasum
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
