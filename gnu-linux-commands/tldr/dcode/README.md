# dcode

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/dcode/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
dcfldd
,
pv
,
logstash
,
runsv
,
tlmgr check
.
dcode
Recursively detect and decode strings, supporting hex, decimal, binary, base64, URL, FromChar encodings, Caesar ciphers, and MD5, SHA1, and SHA2 hashes.
Warning: uses 3rd-party web services for MD5, SHA1 and SHA2 hash lookups. For sensitive data, use
-s
to avoid these services.
More information:
https://github.com/s0md3v/Decodify
.
Recursively detect and decode a string:
dcode "{{NjM3YTQyNzQ1YTQ0NGUzMg==}}"
Rotate a string by the specified offset:
dcode -rot {{11}} "{{spwwz hzcwo}}"
Rotate a string by all 26 possible offsets:
dcode -rot {{all}} "{{bpgkta xh qtiitg iwpc sr}}"
Reverse a string:
dcode -rev "{{hello world}}"
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
