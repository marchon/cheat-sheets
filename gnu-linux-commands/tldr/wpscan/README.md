# wpscan

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/wpscan/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
pastel
,
pueue status
,
mmdc
,
spike
.
wpscan
WordPress vulnerability scanner.
More information:
https://github.com/wpscanteam/wpscan
.
Update the vulnerability database:
wpscan --update
Scan a WordPress website:
wpscan --url {{url}}
Scan a WordPress website, using random user agents and passive detection:
wpscan --url {{url}} --stealthy
Scan a WordPress website, checking for vulnerable plugins and specifying the path to the
wp-content
directory:
wpscan --url {{url}} --enumerate {{vp}} --wp-content-dir {{remote/path/to/wp-content}}
Scan a WordPress website through a proxy:
wpscan --url {{url}} --proxy {{protocol://ip:port}} --proxy-auth {{username:password}}
Perform user identifiers enumeration on a WordPress website:
wpscan --url {{url}} --enumerate {{u}}
Execute a password guessing attack on a WordPress website:
wpscan --url {{url}} --usernames {{username|path/to/usernames.txt}} --passwords {{path/to/passwords.txt}} threads {{20}}
Scan a WordPress website, collecting vulnerability data from the WPVulnDB (https://wpvulndb.com/):
wpscan --url {{url}} --api-token {{token}}
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
