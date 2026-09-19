# gpg2

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gpg2/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
openssl ts
,
du
,
dotnet publish
.
gpg2
GNU Privacy Guard 2.
See
gpg
for GNU Privacy Guard 1.
More information:
https://docs.releng.linuxfoundation.org/en/latest/gpg.html
.
List imported keys:
gpg2 --list-keys
Encrypt a specified file for a specified recipient, writing the output to a new file with
.gpg
appended:
gpg2 --encrypt --recipient {{alice@example.com}} {{path/to/doc.txt}}
Encrypt a specified file with only a passphrase, writing the output to a new file with
.gpg
appended:
gpg2 --symmetric {{path/to/doc.txt}}
Decrypt a specified file, writing the result to the standard output:
gpg2 --decrypt {{path/to/doc.txt.gpg}}
Import a public key:
gpg2 --import {{path/to/public_key.gpg}}
Export the public key of a specified email address to the standard output:
gpg2 --export --armor {{alice@example.com}}
Export the private key with a specified email address to the standard output:
gpg2 --export-secret-keys --armor {{alice@example.com}}
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
