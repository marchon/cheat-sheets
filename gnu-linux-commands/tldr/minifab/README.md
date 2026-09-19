# minifab

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/minifab/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dune
,
xetex
,
st flash
,
u3d
,
ansible inventory
.
minifab
Utility tool that automates the setup and deployment of Hyperledger Fabric networks.
More information:
https://github.com/hyperledger-labs/minifabric
.
Bring up the default Hyperledger Fabric network:
minifab up -i {{minifab_version}}
Bring down the Hyperledger Fabric network:
minifab down
Install chaincode onto a specified channel:
minifab install -n {{chaincode_name}}
Install a specific chaincode version onto a channel:
minifab install -n {{chaincode_name}} -v {{chaincode_version}}
Initialize the chaincode after installation/upgrade:
minifab approve,commit,initialize,discover
Invoke a chaincode method with the specified arguments:
minifab invoke -n {{chaincode_name}} -p '"{{method_name}}", "{{arg0}}", "{{arg1}}", ...'
Make a query on the ledger:
minifab blockquery {{block_number}}
Quickly run an application:
minifab apprun -l {{app_programming_langauge}}
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
