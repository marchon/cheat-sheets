# dvc-config

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dvc-config/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
uncrustify
,
git submodule
,
gh release
.
dvc config
Low level command to manage custom configuration options for dvc repositories.
These configurations can be on project, local, global, or system level.
More information:
https://dvc.org/doc/command-reference/config
.
Get the name of the default remote:
dvc config core.remote
Set the project's default remote:
dvc config core.remote {{remote_name}}
Unset the project's default remote:
dvc config --unset core.remote
Get the config value for a specified key for the current project:
dvc config {{key}}
Set the config value for a key on a project level:
dvc config {{key}} {{value}}
Unset a project level config value for a given key:
dvc config --unset {{key}}
Set a local, global, or system level config value:
dvc config --local/global/system {{key}} {{value}}
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
