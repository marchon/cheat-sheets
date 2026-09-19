# ssh-keygen

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ssh-keygen/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hg push
,
git cherry pick
,
virt sparsify
.
ssh-keygen
Generate ssh keys used for authentication, password-less logins, and other things.
More information:
https://man.openbsd.org/ssh-keygen
.
Generate a key interactively:
ssh-keygen
Specify file in which to save the key:
ssh-keygen -f {{~/.ssh/filename}}
Generate an ed25519 key with 100 key derivation function rounds:
ssh-keygen -t {{ed25519}} -a {{100}}
Generate an RSA 4096-bit key with email as a comment:
ssh-keygen -t {{dsa|ecdsa|ed25519|rsa}} -b {{4096}} -C "{{comment|email}}"
Remove the keys of a host from the known_hosts file (useful when a known host has a new key):
ssh-keygen -R {{remote_host}}
Retrieve the fingerprint of a key in MD5 Hex:
ssh-keygen -l -E {{md5}} -f {{~/.ssh/filename}}
Change the password of a key:
ssh-keygen -p -f {{~/.ssh/filename}}
Change the type of the key format (for example from OPENSSH format to PEM), the file will be rewritten in-place:
ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/OpenSSH_private_key}}
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
