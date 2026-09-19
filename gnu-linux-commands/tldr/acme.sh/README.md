# acme.sh

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/acme.sh/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
patchwork
,
fluxctl
,
phpstorm
.
acme.sh
Shell script implementing ACME client protocol, an alternative to certbot.
See also
acme.sh dns
.
More information:
https://github.com/acmesh-official/acme.sh
.
Issue a certificate using webroot mode:
acme.sh --issue --domain {{example.com}} --webroot {{/path/to/webroot}}
Issue a certificate for multiple domains using standalone mode using port 80:
acme.sh --issue --standalone --domain {{example.com}} --domain {{www.example.com}}
Issue a certificate using standalone TLS mode using port 443:
acme.sh --issue --alpn --domain {{example.com}}
Issue a certificate using a working Nginx configuration:
acme.sh --issue --nginx --domain {{example.com}}
Issue a certificate using a working Apache configuration:
acme.sh --issue --apache --domain {{example.com}}
Issue a wildcard (\*) certificate using an automatic DNS API mode:
acme.sh --issue --dns {{dns_cf}} --domain {{*.example.com}}
Install certificate files into the specified locations (useful for automatic certificate renewal):
acme.sh --install-cert -d {{example.com}} --key-file {{/path/to/example.com.key}} --fullchain-file {{/path/to/example.com.cer}} --reloadcmd {{"systemctl force-reload nginx"}}
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
