# sops

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sops/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
handbrakecli
,
kube fzf
,
gh mintty
.
sops
SOPS: Secrets OPerationS.
Tool for managing secrets.
More information:
https://github.com/mozilla/sops
.
Encrypt a file:
sops -e {{path/to/myfile.json}} > {{path/to/myfile.enc.json}}
Decrypt a file to the standard output:
sops -d {{path/to/myfile.enc.json}}
Rotate data keys for a sops file:
sops -r {{path/to/myfile.enc.yaml}}
Change the extension of the file once encrypted:
sops -d --input-type json {{path/to/myfile.enc.json}}
Extract keys by naming them, and array elements by numbering them:
sops -d --extract '["an_array"][1]' {{path/to/myfile.enc.json}}
Show the difference between two sops files:
diff <(sops -d {{path/to/secret1.enc.yaml}}) <(sops -d {{path/to/secret2.enc.yaml}})
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
