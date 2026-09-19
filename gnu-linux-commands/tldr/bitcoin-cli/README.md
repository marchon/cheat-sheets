# bitcoin-cli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bitcoin-cli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mlr
,
sup
,
pueue log
,
gcal
,
godoc
.
bitcoin-cli
Command-line client to interact with the Bitcoin daemon via RPC calls.
Uses the configuration defined in
bitcoin.conf
.
More information:
https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments
.
Send a transaction to a given address:
bitcoin-cli sendtoaddress "{{address}}" {{amount}}
Generate one or more blocks:
bitcoin-cli generate {{num_blocks}}
Print high-level information about the wallet:
bitcoin-cli getwalletinfo
List all outputs from previous transactions available to fund outgoing transactions:
bitcoin-cli listunspent
Export the wallet information to a text file:
bitcoin-cli dumpwallet "{{path/to/file}}"
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
