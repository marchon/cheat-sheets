# evil-winrm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/evil-winrm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mkvmerge
,
vlc
,
lynx
,
ical
,
tye
,
exiftool
.
evil-winrm
Windows Remote Management (WinRM) shell for pentesting.
Once connected, we get a PowerShell prompt on the target host.
More information:
https://github.com/Hackplayers/evil-winrm
.
Connect to a host:
evil-winrm --ip {{ip}} --user {{user}} --password {{password}}
Connect to a host, passing the password hash:
evil-winrm --ip {{ip}} --user {{user}} --hash {{nt_hash}}
Connect to a host, specifying directories for scripts and executables:
evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --scripts {{path/to/scripts}} --executables {{path/to/executables}}
Connect to a host, using SSL:
evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --ssl --pub-key {{path/to/pubkey}} --priv-key {{path/to/privkey}}
Upload a file to the host:
PS > upload {{path/to/local/file}} {{path/to/remote/file}}
Get a list of loaded PowerShell functions:
PS > menu
Load a PowerShell script from the
--scripts
directory:
PS > {{script.ps1}}
Invoke a binary on the host from the
--executables
directory:
PS > Invoke-Binary {{binary.exe}}
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
