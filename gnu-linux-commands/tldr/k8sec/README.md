# k8sec

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/k8sec/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
timetrap
,
magento
,
ntl
,
tar
,
nms
.
k8sec
Command-line interface tool to manage Kubernetes secrets.
More information:
https://github.com/dtan4/k8sec
.
List all secrets:
k8sec list
List a specific secret as a base64-encoded string:
k8sec list {{secret_name}} --base64
Set a secret's value:
k8sec set {{secret_name}} {{key=value}}
Set a base64-encoded value:
k8sec set --base64 {{secret_name}} {{key=encoded_value}}
Unset a secret:
k8sec unset {{secret_name}}
Load secrets from a file:
k8sec load -f {{path/to/file}} {{secret_name}}
Dump secrets to a file:
k8sec dump -f {{path/to/file}} {{secret_name}}
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
