# svn

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/svn/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git checkout index
,
openssl genpkey
.
svn
Subversion command-line client tool.
More information:
https://subversion.apache.org
.
Check out a working copy from a repository:
svn co {{url/to/repository}}
Bring changes from the repository into the working copy:
svn up
Put files and directories under version control, scheduling them for addition to repository. They will be added in next commit:
svn add {{PATH}}
Send changes from your working copy to the repository:
svn ci -m {{commit_log_message}} [{{PATH}}]
Display changes from the last 10 revisions, showing modified files for each revision:
svn log -vl {{10}}
Show detailed help:
svn help
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
