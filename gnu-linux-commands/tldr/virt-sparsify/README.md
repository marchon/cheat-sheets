# virt-sparsify

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virt-sparsify/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pdfgrep
,
xml select
,
rbt
,
pfetch
.
virt-sparsify
Make virtual machine drive images thin-provisioned.
NOTE: Use only for offline machines to avoid data corruption.
Home page:
https://libguestfs.org/
.
Create a sparsified compressed image without snapshots from an unsparsified one:
virt-sparsify --compress {{path/to/image.qcow2}} {{path/to/image_new.qcow2}}
Sparsify an image in-place:
virt-sparsify --in-place {{path/to/image.img}}
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
