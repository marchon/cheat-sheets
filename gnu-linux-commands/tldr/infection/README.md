# infection

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/infection/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sendmail
,
mh_metric
,
coffee
,
terraform
.
infection
A mutation testing framework for PHP.
More information:
https://infection.github.io
.
Analyze code using the configuration file (or create one if it does not exist):
infection
Use a specific number of threads:
infection --threads {{number_of_threads}}
Specify a minimum Mutation Score Indicator (MSI):
infection --min-msi {{percentage}}
Specify a minimum covered code MSI:
infection --min-covered-msi {{percentage}}
Use a specific test framework (defaults to PHPUnit):
infection --test-framework {{phpunit|phpspec}}
Only mutate lines of code that are covered by tests:
infection --only-covered
Display the mutation code that has been applied:
infection --show-mutations
Specify the log verbosity:
infection --log-verbosity {{default|all|none}}
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
