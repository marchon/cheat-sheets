# aws-ses

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-ses/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
az storage entity
,
sha384sum
.
aws ses
CLI for AWS Simple Email Service.
High-scale inbound and outbound cloud email service.
More information:
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html
.
Create a new receipt rule set:
aws ses create-receipt-rule-set --rule-set-name {{rule_set_name}} --generate-cli-skeleton
Describe the active receipt rule set:
aws ses describe-active-receipt-rule-set --generate-cli-skeletion
Describe a specific receipt rule:
aws ses describe-receipt-rule --rule-set-name {{rule_set_name}} --rule-name {{rule_name}} --generate-cli-skeleton
List all receipt rule sets:
aws ses list-receipt-rule-sets --starting-token {{token_string}} --max-items {{integer}} --generate-cli-skeleton
Delete a specific receipt rule set (the currently active rule set cannot be deleted):
aws ses delete-receipt-rule-set --rule-set-name {{rule_set_name}} --generate-cli-skeleton
Delete a specific receipt rule:
aws ses delete-receipt-rule --rule-set-name {{rule_set_name}} --rule-name {{rule_name}} --generate-cli-skeleton
Send an email:
aws ses send-email --from {{from_address}} --destination "ToAddresses={{addresses}}" --message "Subject={Data={{subject_text}},Charset=utf8},Body={Text={Data={{body_text}},Charset=utf8},Html={Data={{message_body_containing_html}},Charset=utf8}}"
Show help for a specific SES subcommand:
aws ses {{subcommand}} help
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
