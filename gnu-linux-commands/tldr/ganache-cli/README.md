# ganache-cli

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ganache-cli/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
llvm ar
,
john
,
cups config
,
rg
.
ganache-cli
Command-line version of Ganache, your personal blockchain for Ethereum development.
More information:
https://www.trufflesuite.com/ganache
.
Run Ganache:
ganache-cli
Run Ganache with a specific number of accounts:
ganache-cli --accounts={{number_of_accounts}}
Run Ganache and lock available accounts by default:
ganache-cli --secure
Run Ganache server and unlock specific accounts:
ganache-cli --secure --unlock "{{account_private_key1}}" --unlock "{{account_private_key2}}"
Run Ganache with a specific account and balance:
ganache-cli --account="{{account_private_key}},{{account_balance}}"
Run Ganache with accounts with a default balance:
ganache-cli --defaultBalanceEther={{default_balance}}
Run Ganache and log all requests to stdout:
ganache-cli --verbose
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
