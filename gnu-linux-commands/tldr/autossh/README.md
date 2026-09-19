# autossh

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/autossh/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
emulator
,
solo
,
jhsdb
,
uvicorn
.
autossh
Run, monitor and restart SSH connections.
Auto-reconnects to keep port forwarding tunnels up. Accepts all
ssh
flags.
More information:
https://www.harding.motd.ca/autossh
.
Start an SSH session, restarting when a monitoring port fails to return data:
autossh -M {{monitor_port}} "{{ssh_command}}"
Forward a local port to a remote one, restarting when necessary:
autossh -M {{monitor_port}} -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}
Fork
autossh
into the background before executing
ssh
and don't open a remote shell:
autossh -f -M {{monitor_port}} -N "{{ssh_command}}"
Run in the background, with no monitoring port, and instead send SSH keep-alive packets every 10 seconds to detect failure:
autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{ssh_command}}"
Run in the background, with no monitoring port and no remote shell, exiting if the port forward fails:
autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}
Run in the background, logging
autossh
debug output and
ssh
verbose output to files:
AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{path/to/autossh_log_file.log}} autossh -f -M {{monitor_port}} -v -E {{path/to/ssh_log_file.log}} {{ssh_command}}
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
