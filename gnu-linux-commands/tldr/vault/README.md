# vault

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/vault/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az account
,
you get
,
stty
,
tailscale ssh
.
vault
A CLI to interact with HashiCorp Vault.
More information:
https://www.vaultproject.io/docs/commands
.
Connect to a Vault server and initialize a new encrypted data store:
vault init
Unseal (unlock) the vault, by providing one of the key shares needed to access the encrypted data store:
vault unseal {{key-share-x}}
Authenticate the CLI client against the Vault server, using an authentication token:
vault auth {{authentication_token}}
Store a new secret in the vault, using the generic back-end called "secret":
vault write secret/{{hello}} value={{world}}
Read a value from the vault, using the generic back-end called "secret":
vault read secret/{{hello}}
Read a specific field from the value:
vault read -field={{field_name}} secret/{{hello}}
Seal (lock) the Vault server, by removing the encryption key of the data store from memory:
vault seal
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
