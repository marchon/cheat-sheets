# dokku

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dokku/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git sizer
,
asar
,
gacutil
,
makensis
.
dokku
Docker powered mini-Heroku (PaaS).
Easily deploy multiple apps to your server in different languages using a single
git-push
command.
More information:
https://github.com/dokku/dokku
.
List running apps:
dokku apps
Create an app:
dokku apps:create {{app_name}}
Remove an app:
dokku apps:destroy {{app_name}}
Install plugin:
dokku plugin:install {{full_repo_url}}
Link database to an app:
dokku {{db}}:link {{db_name}} {{app_name}}
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
