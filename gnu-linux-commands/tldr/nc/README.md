# nc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
firefox
,
clj
,
http server upload
.
nc
Netcat is a versatile utility for working with TCP or UDP data.
More information:
https://nmap.org/ncat
.
Listen on a specified port and print any data received:
nc -l {{port}}
Connect to a certain port:
nc {{ip_address}} {{port}}
Set a timeout:
nc -w {{timeout_in_seconds}} {{ipaddress}} {{port}}
Keep the server up after the client detaches:
nc -k -l {{port}}
Keep the client up even after EOF:
nc -q {{timeout}} {{ip_address}}
Scan the open ports of a specified host:
nc -v -z {{ip_address}} {{port}}
Act as proxy and forward data from a local TCP port to the given remote host:
nc -l {{local_port}} | nc {{hostname}} {{remote_port}}
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
