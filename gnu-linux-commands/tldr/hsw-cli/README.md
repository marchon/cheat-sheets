# hsw-cli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hsw-cli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
jupytext
,
pueue edit
,
git diff
.
hsw-cli
The command-line REST tool for the Handshake wallet.
More information:
https://github.com/handshake-org/hs-client
.
Unlock the current wallet (timeout in seconds):
hsw-cli unlock {{passphrase}} {{timeout}}
Lock the current wallet:
hsw-cli lock
View the current wallet's details:
hsw-cli get
View the current wallet's balance:
hsw-cli balance
View the current wallet's transaction history:
hsw-cli history
Send a transaction with the specified coin amount to an address:
hsw-cli send {{address}} {{1.05}}
View the current wallet's pending transactions:
hsw-cli pending
View details about a transaction:
hsw-cli tx {{transaction_hash}}
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
