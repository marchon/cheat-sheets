# tea

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tea/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hostname
,
kitex
,
git log
,
dotnet tool
.
tea
A command-line tool to interact with Gitea servers.
More information:
https://gitea.com/gitea/tea
.
Log into a Gitea server:
tea login add --name "{{name}}" --url "{{url}}" --token "{{token}}"
Display all repositories:
tea repos ls
Display a list of issues:
tea issues ls
Display a list of issues for a specific repository:
tea issues ls --repo "{{repository}}"
Create a new issue:
tea issues create --title "{{title}}" --body "{{body}}"
Display a list of open pull requests:
tea pulls ls
Open the current repository in a browser:
tea open
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
