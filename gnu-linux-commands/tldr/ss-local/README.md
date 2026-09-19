# ss-local

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ss-local/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pueue remove
,
virt sparsify
.
ss-local
Run a Shadowsocks client as a SOCKS5 proxy.
More information:
https://github.com/shadowsocks/shadowsocks-libev/blob/master/doc/ss-local.asciidoc
.
Run a Shadowsocks proxy by specifying the host, server port, local port, password, and encryption method:
ss-local -s {{host}} -p {{server_port}} -l {{local port}} -k {{password}} -m {{encrypt_method}}
Run a Shadowsocks proxy by specifying the config file:
ss-local -c {{path/to/config/file.json}}
Use a plugin to run the proxy client:
ss-local --plugin {{plugin_name}} --plugin-opts {{plugin_options}}
Enable TCP fast open:
ss-local --fast-open
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
