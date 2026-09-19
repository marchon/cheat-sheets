# openssl-dgst

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/openssl-dgst/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
paci
,
typeorm
,
makensis
,
mupdf
.
openssl dgst
OpenSSL command to generate digest values and perform signature operations.
More information:
https://www.openssl.org/docs/manmaster/man1/openssl-dgst.html
.
Calculate the SHA256 digest for a file, saving the result to a specific file:
openssl dgst -sha256 -binary -out {{output_file}} {{input_file}}
Sign a file using an RSA key, saving the result to a specific file:
openssl dgst -sign {{private_key_file}} -sha256 -sigopt rsa_padding_mode:pss -out {{output_file}} {{input_file}}
Verify an RSA signature:
openssl dgst -verify {{public_key_file}} -signature {{signature_file}} -sigopt rsa_padding_mode:pss {{signature_message_file}}
Sign a file using and ECDSA key:
openssl dgst -sign {{private_key_file}} -sha256 -out {{output_file}} {{input_file}}
Verify an ECDSA signature:
openssl dgst -verify {{public_key_file}} -signature {{signature_file}} {{signature_message_file}}
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
