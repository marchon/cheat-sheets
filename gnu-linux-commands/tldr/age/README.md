# age

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/age/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
go fmt
,
patch
,
timew
,
middleman
.
age
A simple, modern and secure file encryption tool.
More information:
https://age-encryption.org
.
Generate an encrypted file that can be decrypted with a passphrase:
age --passphrase --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}
Generate a key pair, saving the private key to an unencrypted file and printing the public key to stdout:
age-keygen --output {{path/to/file}}
Encrypt a file with one or more public keys that are entered as literals:
age --recipient {{public_key_1}} --recipient {{public_key_2}} {{path/to/unencrypted_file}} --output {{path/to/encrypted_file}}
Encrypt a file with one or more public keys that are specified in a recipients file:
age --recipients-file {{path/to/recipients_file}} {{path/to/unencrypted_file}} --output {{path/to/encrypted_file}}
Decrypt a file with a passphrase:
age --decrypt --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}
Decrypt a file with a private key file:
age --decrypt --identity {{path/to/private_key_file}} --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}
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
