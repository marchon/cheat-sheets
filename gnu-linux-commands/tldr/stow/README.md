# stow

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/stow/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
bq
,
dc
,
pio remote
,
pyenv
,
dvc gc
.
stow
Symlink manager.
Often used to manage dotfiles.
More information:
https://www.gnu.org/software/stow
.
Symlink all files recursively to a given directory:
stow --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}
Delete symlinks recursively from a given directory:
stow --delete --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}
Simulate to see what the result would be like:
stow --simulate --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}
Delete and resymlink:
stow --restow --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}
Exclude files matching a regular expression:
stow --ignore={{regular_expression}} --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}
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
