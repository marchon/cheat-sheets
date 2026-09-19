# openssl-genpkey

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/openssl-genpkey/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gunicorn
,
ajson
,
nmap
,
cabal
,
expose
.
openssl genpkey
OpenSSL command to generate asymmetric key pairs.
More information:
https://www.openssl.org/docs/manmaster/man1/openssl-genpkey.html
.
Generate an RSA private key of 2048 bits, saving it to a specific file:
openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:{{2048}} -out {{filename.key}}
Generate an elliptic curve private key using the curve
prime256v1
, saving it to a specific file:
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:{{prime256v1}} -out {{filename.key}}
Generate an
ED25519
elliptic curve private key, saving it to a specific file:
openssl genpkey -algorithm {{ED25519}} -out {{filename.key}}
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
