# gh-api

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gh-api/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gh run
,
git repl
,
k6
,
docker ps
.
gh api
Makes authenticated HTTP requests to the GitHub API and prints the response.
More information:
https://cli.github.com/manual/gh_api
.
Display the subcommand help:
gh api --help
Display the releases for the current repository in JSON format:
gh api repos/:owner/:repo/releases
Create a reaction for a specific issue:
gh api --header {{Accept:application/vnd.github.squirrel-girl-preview+json}} --raw-field '{{content=+1}}' {{repos/:owner/:repo/issues/123/reactions}}
Display the result of a GraphQL query in JSON format:
gh api graphql --field {{name=':repo'}} --raw-field '{{query}}'
Send a request using a custom HTTP method:
gh api --method {{POST}} {{endpoint}}
Include the HTTP response headers in the output:
gh api --include {{endpoint}}
Do not print the response body:
gh api --silent {{endpoint}}
Send a request to a specific GitHub Enterprise Server:
gh api --hostname {{github.example.com}} {{endpoint}}
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
