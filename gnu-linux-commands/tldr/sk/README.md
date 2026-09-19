# sk

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sk/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
drush
,
glab mr
,
clang tidy
,
avo
.
sk
Fuzzy finder written in Rust.
Similar to
fzf
.
More information:
https://github.com/lotabout/skim
.
Start skim on all files in the specified directory:
find {{path/to/directory}} -type f | sk
Start skim for running processes:
ps aux | sk
Start skim with a specified query:
sk --query "{{query}}"
Select multiple files with
Shift + Tab
and write to a file:
find {{path/to/directory}} -type f | sk --multi > {{filename}}
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
