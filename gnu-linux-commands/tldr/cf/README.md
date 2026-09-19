# cf

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cf/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
llvm cat
,
rr
,
hg update
,
semver
.
cf
Command-line tool to manage apps and services on Cloud Foundry.
More information:
https://docs.cloudfoundry.org
.
Push an app using the default settings:
cf push {{app_name}}
View the services available from your organization:
cf marketplace
Create a service instance:
cf create-service {{service}} {{plan}} {{service_name}}
Connect an application to a service:
cf bind-service {{app_name}} {{service_name}}
Run a script whose code is included in the app, but runs independently:
cf run-task {{app_name}} "{{script_command}}" --name {{task_name}}
Start an interactive SSH session with a VM hosting an app:
cf ssh {{app_name}}
View a dump of recent app logs:
cf logs {{app_name}} --recent
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
