# puppet-agent

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/puppet-agent/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
airmon ng
,
ssh agent
,
vimtutor
.
puppet agent
Retrieves the client configuration from a Puppet server and applies it to the local host.
More information:
https://puppet.com/docs/puppet/7/man/agent.html
.
Register a node at a Puppet server and apply the received catalog:
puppet agent --test --server {{puppetserver_fqdn}} --serverport {{port}} --waitforcert {{poll_time}}
Run the agent in the background (uses settings from
puppet.conf
):
puppet agent
Run the agent once in the foreground, then exit:
puppet agent --test
Run the agent in dry-mode:
puppet agent --test --noop
Log every resource being evaluated (even if nothing is being changed):
puppet agent --test --evaltrace
Disable the agent:
puppet agent --disable "{{message}}"
Enable the agent:
puppet agent --enable
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
