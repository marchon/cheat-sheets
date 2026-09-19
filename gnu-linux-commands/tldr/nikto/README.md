# nikto

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nikto/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
testssl
,
sd
,
espeak
,
dotnet ef
.
nikto
Web server scanner which performs tests against web servers for multiple items.
More information:
https://cirt.net/Nikto2
.
Perform a basic Nikto scan against a target host:
perl nikto.pl -h {{192.168.0.1}}
Specify the port number when performing a basic scan:
perl nikto.pl -h {{192.168.0.1}} -p {{443}}
Scan ports and protocols with full URL syntax:
perl nikto.pl -h {{https://192.168.0.1:443/}}
Scan multiple ports in the same scanning session:
perl nikto.pl -h {{192.168.0.1}} -p {{80,88,443}}
Update to the latest plugins and databases:
perl nikto.pl -update
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
