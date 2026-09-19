# pm2

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/pm2/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cargo clippy
,
rails routes
.
pm2
Process manager for Node.js.
Used for log management, monitoring and configuring processes.
More information:
https://pm2.keymetrics.io
.
Start a process with a name that can be used for later operations:
pm2 start {{app.js}} --name {{myapp}}
List processes:
pm2 list
Monitor all processes:
pm2 monit
Stop a process:
pm2 stop {{myapp}}
Restart a process:
pm2 restart {{myapp}}
Dump all processes for resurrecting them later:
pm2 save
Resurrect previously dumped processes:
pm2 resurrect
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
