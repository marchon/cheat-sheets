# todoist

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/todoist/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
expose
,
zellij
,
pg_dump
,
elixir
.
todoist
Access Todoist from the command-line.
More information:
https://github.com/sachaos/todoist
.
Add a task:
todoist add "{{task_name}}"
Add a high priority task with a label, project, and due date:
todoist add "{{task_name}}" --priority {{1}} --label-ids "{{label_id}}" --project-name "{{project_name}}" --date "{{tmr 9am}}"
Add a high priority task with a label, project, and due date in quick mode:
todoist quick '#{{project_name}} "{{tmr 9am}}" p{{1}} {{task_name}} @{{label_name}}'
List all tasks with a header and color:
todoist --header --color list
List all high priority tasks:
todoist list --filter p{{1}}
List today's tasks with high priority that have the specified label:
todoist list --filter '(@{{label_name}} | {{today}}) & p{{1}}'
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
