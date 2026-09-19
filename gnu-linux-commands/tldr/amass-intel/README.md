# amass-intel

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/amass-intel/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
tbl
,
swipl
,
sails
,
terragrunt
,
sha1sum
.
amass intel
Collect open source intel on an organisation like root domains and ASNs.
More information:
https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-intel-subcommand
.
Find root domains in an IP address range:
amass intel -addr {{192.168.0.1-254}}
Use active recon methods:
amass intel -active -addr {{192.168.0.1-254}}
Find root domains related to a domain:
amass intel -whois -d {{domain_name}}
Find ASNs belonging to an organisation:
amass intel -org {{organisation_name}}
Find root domains belonging to a given Autonomous System Number:
amass intel -asn {{asn}}
Save results to a text file:
amass intel -o {{output_file}} -whois -d {{domain_name}}
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
