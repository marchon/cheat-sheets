# rtmpdump

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rtmpdump/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gibo
,
piodebuggdb
,
xml transform
.
rtmpdump
A tool to dump media content streamed over the RTMP protocol.
More information:
http://rtmpdump.mplayerhq.hu/
.
Download a file:
rtmpdump --rtmp {{rtmp://example.com/path/to/video}} -o {{file.ext}}
Download a file from a Flash player:
rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --swfVfy {{http://example.com/player}} --flashVer "{{LNX 10,0,32,18}}" -o {{file.ext}}
Specify connection parameters if they are not detected correctly:
rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --app {{app_name}} --playpath {{path/to/video}} -o {{file.ext}}
Download a file from a server that requires a referrer:
rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --pageUrl {{http://example.com/webpage}} -o {{file.ext}}
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
