# pass

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pass/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
csvtool
,
texdoc
,
mk
,
npx
,
wat2wasm
.
pass
Tool for storing and reading passwords or other sensitive data.
All data is GPG-encrypted, and managed with a Git repository.
More information:
https://www.passwordstore.org
.
Initialize (or re-encrypt) the storage using one or more GPG IDs:
pass init {{gpg_id_1}} {{gpg_id_2}}
Save a new password and additional information (press Ctrl + D on a new line to complete):
pass insert --multiline {{path/to/data}}
Edit an entry:
pass edit {{path/to/data}}
Copy a password (first line of the data file) to the clipboard:
pass -c {{path/to/data}}
List the whole store tree:
pass
Generate a new random password with a given length, and copy it to the clipboard:
pass generate -c {{path/to/data}} {{num}}
Initialize a new Git repository (any changes done by pass will be committed automatically):
pass git init
Run a Git command on behalf of the password storage:
pass git {{command}}
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
