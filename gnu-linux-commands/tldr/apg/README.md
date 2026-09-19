# apg

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/apg/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
task
,
git restore
,
ninja
,
odps func
.
apg
Creates arbitrarily complex random passwords.
More information:
https://manned.org/apg
.
Create random passwords (default password length is 8):
apg
Create a password with at least 1 symbol (S), 1 number (N), 1 uppercase (C), 1 lowercase (L):
apg -M SNCL
Create a password with 16 characters:
apg -m {{16}}
Create a password with maximum length of 16:
apg -x {{16}}
Create a password that doesn't appear in a dictionary (the dictionary file has to be provided):
apg -r {{dictionary_file}}
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
