# git-notes

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/git-notes/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
fselect
,
phpenv
,
phpmd
,
pio test
.
git notes
Add or inspect object notes.
More information:
https://git-scm.com/docs/git-notes
.
List all notes and the objects they are attached to:
git notes list
List all notes attached to a given object (defaults to HEAD):
git notes list [{{object}}]
Show the notes attached to a given object (defaults to HEAD):
git notes show [{{object}}]
Append a note to a specified object (opens the default text editor):
git notes append {{object}}
Append a note to a specified object, specifying the message:
git notes append --message="{{message_text}}"
Edit an existing note (defaults to HEAD):
git notes edit [{{object}}]
Copy a note from one object to another:
git notes copy {{source_object}} {{target_object}}
Remove all the notes added to a specified object:
git notes remove {{object}}
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
