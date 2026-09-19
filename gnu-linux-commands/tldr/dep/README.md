# dep

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dep/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mysql
,
git stage
,
consul
,
xml transform
.
dep
A CLI tool for deployment of PHP applications.
Note: The Go command
dep
with the same name is deprecated and archived.
More information:
https://deployer.org
.
Interactively initialize deployer in the local path (use a framework template with
--template={{template}}
):
dep init
Deploy an application to a remote host:
dep deploy {{hostname}}
Rollback to the previous working release:
dep rollback
Connect to a remote host via ssh:
dep ssh {{hostname}}
List commands:
dep list
Run any arbitrary command on the remote hosts:
dep run "{{command}}"
Display help for a command:
dep help {{command}}
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
