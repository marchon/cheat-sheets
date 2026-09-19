# in-toto-record

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/in-toto-record/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
grip
,
screen
,
git daemon
,
zless
.
in-toto-record
Create a signed link metadata file to provide evidence for supply chain steps.
More information:
https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-record.html
.
Start the record (creates a preliminary link file):
in-toto-record start -n {{edit-files}} -k {{path/to/key_file}} -m {{.}}
Stop the record (expects a preliminary link file):
in-toto-record stop -n {{edit-files}} -k {{path/to/key_file}} -p {{.}}
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
