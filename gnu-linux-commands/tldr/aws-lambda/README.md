# aws-lambda

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/aws-lambda/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
whois
,
pwsh
,
calendar
,
gnuplot
.
aws lambda
CLI for AWS lambda.
More information:
https://docs.aws.amazon.com/cli/latest/reference/lambda/
.
Run a function:
aws lambda invoke --function-name {{name}} {{path/to/response}}.json
Run a function with an input payload in JSON format:
aws lambda invoke --function-name {{name}} --payload {{json}} {{path/to/response}}.json
List functions:
aws lambda list-functions
Display the configuration of a function:
aws lambda get-function-configuration --function-name {{name}}
List function aliases:
aws lambda list-aliases --function-name {{name}}
Display the reserved concurrency configuration for a function:
aws lambda get-function-concurrency --function-name {{name}}
List which AWS services can invoke the function:
aws lambda get-policy --function-name {{name}}
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
