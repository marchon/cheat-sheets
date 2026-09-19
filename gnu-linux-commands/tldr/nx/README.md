# nx

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nx/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git rename branch
,
latex
,
pg_restore
.
nx
CLI utility for managing
nx
workspaces.
More information:
https://nx.dev/l/r/getting-started/nx-cli
.
Build a specific project:
nx build {{project}}
Test a specific project:
nx test {{project}}
Execute a target on a specific project:
nx run {{project}}:{{target}}
Execute a target on multiple projects:
nx run-many --target {{target}} --projects {{project1}},{{project2}}
Execute a target on all projects in the workspace:
nx run-many --target {{target}} --all
Execute a target only on projects that have been changed:
nx affected --target {{target}}
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
