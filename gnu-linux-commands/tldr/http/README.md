# http

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/http/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sponge
,
git release
,
roave backward compatibility check
.
http
HTTPie: HTTP client, aims to be easier to use than cURL.
More information:
https://httpie.org
.
Download a URL to a file:
http --download {{example.org}}
Send form-encoded data:
http --form {{example.org}} {{name='bob'}} {{profile_picture@'bob.png'}}
Send JSON object:
http {{example.org}} {{name='bob'}}
Specify an HTTP method:
http {{HEAD}} {{example.org}}
Include an extra header:
http {{example.org}} {{X-MyHeader:123}}
Pass a username and password for server authentication:
http --auth {{username:password}} {{example.org}}
Specify raw request body via stdin:
cat {{data.txt}} | http PUT {{example.org}}
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
