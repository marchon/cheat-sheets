# openssl-x509

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/openssl-x509/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dotnet ef
,
type
,
llvm ar
,
sponge
.
openssl x509
OpenSSL command to manage X.509 certificates.
More information:
https://www.openssl.org/docs/manmaster/man1/openssl-x509.html
.
Display certificate information:
openssl x509 -in {{filename.crt}} -noout -text
Display a certificate's expiration date:
openssl x509 -enddate -noout -in {{filename.pem}}
Convert a certificate between binary DER encoding and textual PEM encoding:
openssl x509 -inform {{der}} -outform {{pem}} -in {{original_certificate_file}} -out {{converted_certificate_file}}
Store a certificate's public key in a file:
openssl x509 -in {{certificate_file}} -noout -pubkey -out {{output_file}}
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
