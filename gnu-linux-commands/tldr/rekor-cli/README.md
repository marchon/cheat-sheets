# rekor-cli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rekor-cli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
glow
,
cargo build
,
ssh copy id
.
rekor-cli
Immutable tamper resistant ledger of metadata generated within a software projects supply chain.
More information:
https://github.com/sigstore/rekor
.
Upload an artifact to Rekor:
rekor-cli upload --artifact {{path/to/file.ext}} --signature {{path/to/file.ext.sig}} --pki-format={{x509}} --public-key={{path/to/key.pub}}
Get information regarding entries in the Transparency Log:
rekor-cli get --uuid={{0e81b4d9299e2609e45b5c453a4c0e7820ac74e02c4935a8b830d104632fd2d1}}
Search the Rekor index to find entries by Artifact:
rekor-cli search --artifact {{path/to/file.ext}}
Search the Rekor index to find entries by a specific hash:
rekor-cli search --sha {{6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b}}
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
