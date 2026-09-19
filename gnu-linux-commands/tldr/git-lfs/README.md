# git-lfs

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-lfs/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fls
,
dvc diff
,
p10k
,
arc
,
x11docker
.
git lfs
Work with large files in Git repositories.
More information:
https://git-lfs.github.com
.
Initialize Git LFS:
git lfs install
Track files that match a glob:
git lfs track '{{*.bin}}'
Change the Git LFS endpoint URL (useful if the LFS server is separate from the Git server):
git config -f .lfsconfig lfs.url {{lfs_endpoint_url}}
List tracked patterns:
git lfs track
List tracked files that have been committed:
git lfs ls-files
Push all Git LFS objects to the remote server (useful if errors are encountered):
git lfs push --all {{remote_name}} {{branch_name}}
Fetch all Git LFS objects:
git lfs fetch
Checkout all Git LFS objects:
git lfs checkout
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
