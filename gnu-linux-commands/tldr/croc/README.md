# croc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/croc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
swipl
,
packtpub
,
base64
,
kaggle
.
croc
Send and receive files easily and securely over any network.
More information:
https://github.com/schollz/croc
.
Send a file or directory:
croc send {{path/to/file_or_directory}}
Send a file or directory with a specific passphrase:
croc send --code {{passphrase}} {{path/to/file_or_directory}}
Receive a file or directory on receiving machine:
croc {{passphrase}}
Send and connect over a custom relay:
croc --relay {{ip_to_relay}} send {{path/to/file_or_directory}}
Receive and connect over a custom relay:
croc --relay {{ip_to_relay}} {{passphrase}}
Host a croc relay on the default ports:
croc relay
Display parameters and options for a croc command:
croc {{send|relay}} --help
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
