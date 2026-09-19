# aws-vault

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-vault/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pamixer
,
dep
,
zsteg
,
logger
,
jetifier
.
aws-vault
A vault for securely storing and accessing AWS credentials in development environments.
More information:
https://github.com/99designs/aws-vault
.
Add credentials to the secure keystore:
aws-vault add {{profile}}
Execute a command with AWS credentials in the environment:
aws-vault exec {{profile}} -- {{aws s3 ls}}
Open a browser window and login to the AWS Console:
aws-vault login {{profile}}
List profiles, along with their credentials and sessions:
aws-vault list
Rotate AWS credentials:
aws-vault rotate {{profile}}
Remove credentials from the secure keystore:
aws-vault remove {{profile}}
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
