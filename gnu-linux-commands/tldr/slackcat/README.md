# slackcat

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/slackcat/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
command
,
kotlinc
,
fswatch
,
wormhole
.
slackcat
Utility for passing files and command output to Slack.
More information:
https://github.com/bcicen/slackcat
.
Post a file to Slack:
slackcat --channel {{channel_name}} {{path/to/file}}
Post a file to Slack with a custom filename:
slackcat --channel {{channel_name}} --filename={{filename}} {{path/to/file}}
Pipe command output to Slack as a text snippet:
{{command}} | slackcat --channel {{channel_name}} --filename={{snippet_name}}
Stream command output to Slack continuously:
{{command}} | slackcat --channel {{channel_name}} --stream
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
