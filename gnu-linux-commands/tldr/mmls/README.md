# mmls

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mmls/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bosh
,
ghc
,
chroma
,
idnits
,
r2e
,
youtube viewer
.
mmls
Display the partition layout of a volume system.
More information:
https://wiki.sleuthkit.org/index.php?title=Mmls
.
Display the partition table stored in an image file:
mmls {{path/to/image_file}}
Display the partition table with an additional column for the partition size:
mmls -B -i {{path/to/image_file}}
Display the partition table in a split EWF image:
mmls -i ewf {{image.e01}} {{image.e02}}
Display nested partition tables:
mmls -t {{nested_table_type}} -o {{offset}} {{path/to/image_file}}
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
