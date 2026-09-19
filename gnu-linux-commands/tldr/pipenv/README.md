# pipenv

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pipenv/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
shasum
,
fswatch
,
leave
,
autossh
.
pipenv
Simple and unified Python development workflow.
Manages packages and the virtual environment for a project.
More information:
https://pypi.org/project/pipenv
.
Create a new project:
pipenv
Create a new project using Python 3:
pipenv --three
Install a package:
pipenv install {{package_name}}
Install all the dependencies for a project:
pipenv install
Install all the dependencies for a project (including dev packages):
pipenv install --dev
Uninstall a package:
pipenv uninstall {{package_name}}
Start a shell within the created virtual environment:
pipenv shell
Generate a
requirements.txt
(list of dependencies) for a project:
pipenv lock --requirements
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
