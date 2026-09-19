# diff

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/diff/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
python3
,
g++
,
ykinfo
,
watson
,
kubectl rollout
.
diff
Compare files and directories.
More information:
https://man7.org/linux/man-pages/man1/diff.1.html
.
Compare files (lists changes to turn
old_file
into
new_file
):
diff {{old_file}} {{new_file}}
Compare files, ignoring white spaces:
diff --ignore-all-space {{old_file}} {{new_file}}
Compare files, showing the differences side by side:
diff --side-by-side {{old_file}} {{new_file}}
Compare files, showing the differences in unified format (as used by
git diff
):
diff --unified {{old_file}} {{new_file}}
Compare directories recursively (shows names for differing files/directories as well as changes made to files):
diff --recursive {{old_directory}} {{new_directory}}
Compare directories, only showing the names of files that differ:
diff --recursive --brief {{old_directory}} {{new_directory}}
Create a patch file for Git from the differences of two text files, treating nonexistent files as empty:
diff --text --unified --new-file {{old_file}} {{new_file}} > {{diff.patch}}
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
