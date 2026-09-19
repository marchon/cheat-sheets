# conda

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/conda/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
espanso
,
mongod
,
pdfunite
,
coffee
.
conda
Package, dependency and environment management for any programming language.
Some subcommands such as
conda create
have their own usage documentation.
More information:
https://github.com/conda/conda
.
Create a new environment, installing named packages into it:
conda create --name {{environment_name}} {{python=3.9 matplotlib}}
List all environments:
conda info --envs
Load an environment:
conda {{activate environment_name}}
Unload an environment:
conda {{deactivate}}
Delete an environment (remove all packages):
conda remove --name {{environment_name}} --all
Install packages into the current environment:
conda install {{python=3.4 numpy}}
List currently installed packages in current environment:
conda list
Delete unused packages and caches:
conda clean --all
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
