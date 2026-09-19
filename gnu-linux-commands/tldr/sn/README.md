# sn

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/sn/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
curl
,
gh
,
if
,
envoy
,
node
,
pdfseparate
.
sn
Mono StrongName utility for signing and verifying IL assemblies.
More information:
https://manned.org/sn
.
Generate a new StrongNaming key:
sn -k {{path/to/key.snk}}
Re-sign an assembly with the specified private key:
sn -R {{path/to/assembly.dll}} {{path/to/key_pair.snk}}
Show the public key of the private key that was used to sign an assembly:
sn -T {{path/to/assembly.exe}}
Extract the public key to a file:
sn -e {{path/to/assembly.dll}} {{path/to/output.pub}}
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
