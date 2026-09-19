# aws-google-auth

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-google-auth/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
circup
,
tar
,
pueue remove
,
php
.
aws-google-auth
Command-line tool to acquire AWS temporary (STS) credentials using Google Apps as a federated (Single Sign-On) provider.
More information:
https://github.com/cevoaustralia/aws-google-auth
.
Log in with Google SSO using the IDP and SP identifiers and set the credentials duration to one hour:
aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}
Log in [a]sking which role to use (in case of several available SAML roles):
aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a
Resolve aliases for AWS accounts:
aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases
Show help information:
aws-google-auth -h
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
