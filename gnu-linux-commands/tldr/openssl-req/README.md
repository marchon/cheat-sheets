# openssl-req

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/openssl-req/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
jq
,
sdiff
,
p10k
,
virtualenv
,
doctl apps
.
openssl req
OpenSSL command to manage PKCS#10 Certificate Signing Requests.
More information:
https://www.openssl.org/docs/manmaster/man1/openssl-req.html
.
Generate a certificate signing request to be sent to a certificate authority:
openssl req -new -sha256 -key {{filename.key}} -out {{filename.csr}}
Generate a self-signed certificate and a corresponding key-pair, storing both in a file:
openssl req -new -x509 -newkey {{rsa}}:{{4096}} -keyout {{filename.key}} -out {{filename.cert}} -subj "{{/C=XX/CN=foobar}}" -days {{365}}
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
