# sqsc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sqsc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git missing
,
mutt
,
lilypond
,
pppd
.
sqsc
A command-line AWS Simple Queue Service client.
More information:
https://github.com/yongfei25/sqsc
.
List all queues:
sqsc lq {{queue_prefix}}
List all messages in a queue:
sqsc ls {{queue_name}}
Copy all messages from one queue to another:
sqsc cp {{source_queue}} {{destination_queue}}
Move all messages from one queue to another:
sqsc mv {{source_queue}} {{destination_queue}}
Describe a queue:
sqsc describe {{queue_name}}
Query a queue with SQL syntax:
sqsc query "SELECT body FROM {{queue_name}} WHERE body LIKE '%user%'"
Pull all messages from a queue into a local SQLite database in your present working directory:
sqsc pull {{queue_name}}
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
