# aws-cur

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-cur/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pio team
,
git show ref
,
graphml2gv
.
aws cur
Create, query, and delete AWS usage report definitions.
More information:
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html
.
Create an AWS cost and usage report definition from a JSON file:
aws cur put-report-definition --report-definition file://{{path/to/report_definition.json}}
List usage report definitions defined for the logged in account:
aws cur describe-report-definitions
Delete a usage report definition:
aws cur --region {{aws_region}} delete-report-definition --report-name {{report}}
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
