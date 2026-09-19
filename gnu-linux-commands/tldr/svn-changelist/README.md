# svn-changelist

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/svn-changelist/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
nc
,
nm
,
calendar
,
rtv
,
git stash
.
svn changelist
Associate a changelist with a set of files.
More information:
http://svnbook.red-bean.com/en/1.7/svn.advanced.changelists.html
.
Add files to a changelist, creating the changelist if it does not exist:
svn changelist {{changelist_name}} {{path/to/file1}} {{path/to/file2}}
Remove files from a changelist:
svn changelist --remove {{path/to/file1}} {{path/to/file2}}
Remove the whole changelist at once:
svn changelist --remove --recursive --changelist {{changelist_name}} .
Add the contents of a space-separated list of directories to a changelist:
svn changelist --recursive {{changelist_name}} {{path/to/directory1}} {{path/to/directory2}}
Commit a changelist:
svn commit --changelist {{changelist_name}}
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
