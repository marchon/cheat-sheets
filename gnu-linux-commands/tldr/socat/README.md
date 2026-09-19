# socat

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/socat/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
lwp request
,
git maintenance
.
socat
Multipurpose relay (SOcket CAT).
More information:
http://www.dest-unreach.org/socat/
.
Listen to a port, wait for an incoming connection and transfer data to STDIO:
socat - TCP-LISTEN:8080,fork
Create a connection to a host and port, transfer data in STDIO to connected host:
socat - TCP4:www.example.com:80
Forward incoming data of a local port to another host and port:
socat TCP-LISTEN:80,fork TCP4:www.example.com:80
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
