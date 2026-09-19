# minisign

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/minisign/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tig
,
trash cli
,
chisel
,
cdk
,
phan
.
minisign
A dead simple tool to sign files and verify signatures.
More information:
https://jedisct1.github.io/minisign/
.
Generate a new keypair at the default location:
minisign -G
Sign a file:
minisign -Sm {{path/to/file}}
Sign a file, adding a trusted (signed) and an untrusted (unsigned) comment in the signature:
minisign -Sm {{path/to/file}} -c "{{Untrusted comment}}" -t "{{Trusted comment}}"
Verify a file and the trusted comments in its signature using the specified public key file:
minisign -Vm {{path/to/file}} -p {{path/to/publickey.pub}}
Verify a file and the trusted comments in its signature, specifying a public key as a Base64 encoded literal:
minisign -Vm {{path/to/file}} -P "{{public_key_base64}}"
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
