# mkcert

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/mkcert/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gpg2
,
git whatchanged
,
valgrind
.
mkcert
Tool for making locally-trusted development certificates.
More information:
https://github.com/FiloSottile/mkcert
.
Install the local CA in the system trust store:
mkcert -install
Generate certificate and private key for a given domain:
mkcert {{example.org}}
Generate certificate and private key for multiple domains:
mkcert {{example.org}} {{myapp.dev}} {{127.0.0.1}}
Generate wildcard certificate and private key for a given domain and its subdomains:
mkcert "{{*.example.it}}"
Uninstall the local CA:
mkcert -uninstall
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
