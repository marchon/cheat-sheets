# ykman

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ykman/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sleep
,
javadoc
,
git cat file
.
ykman
The YubiKey Manager can be used to configure all aspects of the YubiKey.
More information:
https://docs.yubico.com/software/yubikey/tools/ykman/index.html
.
Get information from YubiKey:
ykman info
Get information for a given application from YubiKey:
ykman {{fido|oath|openpgp|otp|piv}} info
Get a list of enabled applications over NFC from YubiKey:
ykman config nfc --list
Enable application over USB on YubiKey:
ykman config usb --enable {{OTP|U2F|FIDO2|OATH|PIV|OPENPGP|HSMAUTH}}
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
