# poetry

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/poetry/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
complete
,
hsw cli
,
zpool
,
llvm dis
.
poetry
Manage Python packages and dependencies.
More information:
https://python-poetry.org/docs
.
Create a new Poetry project in the directory with a specific name:
poetry new {{project_name}}
Install a dependency and its subdependencies:
poetry add {{dependency}}
Install a development dependency and its subdependencies:
poetry add --dev {{dependency}}
Interactively initialize the current directory as a new Poetry project:
poetry init
Get the latest version of all dependencies and update
poetry.lock
:
poetry update
Execute a command inside the project's virtual environment:
poetry run {{command}}
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
