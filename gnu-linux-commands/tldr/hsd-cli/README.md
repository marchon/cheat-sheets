# hsd-cli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/hsd-cli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tabula
,
inkmake
,
jhipster
,
berks
.
hsd-cli
The command-line REST tool for the Handshake blockchain.
More information:
https://handshake.org
.
Retrieve information about the current server:
hsd-cli info
Broadcast a local transaction:
hsd-cli broadcast {{transaction_hex}}
Retrieve a mempool snapshot:
hsd-cli mempool
View a transaction by address or hash:
hsd-cli tx {{address_or_hash}}
View a coin by its hash index or address:
hsd-cli coin {{hash_index_or_address}}
View a block by height or hash:
hsd-cli block {{height_or_hash}}
Reset the chain to the specified block:
hsd-cli reset {{height_or_hash}}
Execute an RPC command:
hsd-cli rpc {{command}} {{args}}
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
