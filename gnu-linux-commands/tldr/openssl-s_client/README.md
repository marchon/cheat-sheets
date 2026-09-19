# openssl-s_client

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/openssl-s_client/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
xkcdpass
,
lilypond
,
ssh
,
textql
.
openssl s_client
OpenSSL command to create TLS client connections.
More information:
https://www.openssl.org/docs/manmaster/man1/openssl-s_client.html
.
Display the start and expiry dates for a domain's certificate:
openssl s_client -connect {{host}}:{{port}} 2>/dev/null | openssl x509 -noout -dates
Display the certificate presented by an SSL/TLS server:
openssl s_client -connect {{host}}:{{port}}
Set the Server Name Indicator (SNI) when connecting to the SSL/TLS server:
openssl s_client -connect {{host}}:{{port}} -servername {{hostname}}
Display the complete certificate chain of an HTTPS server:
openssl s_client -connect {{host}}:443 -showcerts
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
