# virtualenvwrapper

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/virtualenvwrapper/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cake
,
while
,
ngs
,
pdffonts
,
pylint
.
virtualenvwrapper
Group of simple wrapper commands for Python's
virtualenv
tool.
More information:
http://virtualenvwrapper.readthedocs.org
.
Create a new Python
virtualenv
in
$WORKON_HOME
:
mkvirtualenv {{virtualenv_name}}
Create a
virtualenv
for a specific Python version:
mkvirtualenv --python {{/usr/local/bin/python3.8}} {{virtualenv_name}}
Activate or use a different
virtualenv
:
workon {{virtualenv_name}}
Stop the
virtualenv
:
deactivate
List all virtual environments:
lsvirtualenv
Remove a
virtualenv
:
rmvirtualenv {{virtualenv_name}}
Get summary of all virtualenvwrapper commands:
virtualenvwrapper
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
