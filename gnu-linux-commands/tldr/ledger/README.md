# ledger

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ledger/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
assimp
,
aws secretsmanager
.
ledger
Ledger is a powerful, double-entry accounting system that is accessed from the UNIX command-line.
More information:
https://www.ledger-cli.org
.
Print a balance report showing totals:
ledger balance --file {{path/to/ledger.journal}}
List all postings in Expenses ordered by amount:
ledger register {{expenses}} --sorted {{amount}}
Print total Expenses other than Drinks and Food:
ledger balance {{Expenses}} and not ({{Drinks}} or {{Food}})
Print a budget report:
ledger budget
Print summary information about all the postings:
ledger stats
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
