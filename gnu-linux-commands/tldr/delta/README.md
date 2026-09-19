# delta

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/delta/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
crontab
,
fswebcam
,
keychain
,
asar
.
delta
A viewer for Git and diff output.
More information:
https://github.com/dandavison/delta
.
Compare files or directories:
delta {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}
Compare files or directories, showing the line numbers:
delta --line-numbers {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}
Compare files or directories, showing the differences side by side:
delta --side-by-side {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}
Compare files or directories, ignoring any Git configuration settings:
delta --no-gitconfig {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}
Compare, rendering commit hashes, file names, and line numbers as hyperlinks, according to the hyperlink spec for terminal emulators:
delta --hyperlinks {{path/to/old_file_or_directory}} {{path/to/new_file_or_directory}}
Display the current settings:
delta --show-config
Display supported languages and associated file extensions:
delta --list-languages
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
