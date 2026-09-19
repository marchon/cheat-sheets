# git-sed

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-sed/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git rev parse
,
ed
,
logname
,
inkmake
.
git sed
Replace patterns in git-controlled files using sed.
Part of
git-extras
.
More information:
https://github.com/tj/git-extras/blob/master/Commands.md#git-sed
.
Replace the specified text in the current repository:
git sed '{{find_text}}' '{{replace_text}}'
Replace the specified text and then commit the resulting changes with a standard commit message:
git sed -c '{{find_text}}' '{{replace_text}}'
Replace the specified text, using regular expressions:
git sed -f g '{{find_text}}' '{{replace_text}}'
Replace a specific text in all files under a given directory:
git sed '{{find_text}}' '{{replace_text}}' -- {{path/to/directory}}
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
