# xh

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/xh/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
ebook convert
,
lz4
,
cloudflared
.
xh
Friendly and fast tool for sending HTTP requests.
More information:
https://github.com/ducaale/xh
.
Send a GET request:
xh {{httpbin.org/get}}
Send a POST request with a JSON body (key-value pairs are added to a top-level JSON object - e.g.
{"name": "john", "age": 25}
):
xh post {{httpbin.org/post}} {{name=john}} {{age:=25}}
Send a GET request with query parameters (e.g.
first_param=5&second_param=true
):
xh get {{httpbin.org/get}} {{first_param==5}} {{second_param==true}}
Send a GET request with a custom header:
xh get {{httpbin.org/get}} {{header-name:header-value}}
Make a GET request and save the response body to a file:
xh --download {{httpbin.org/json}} --output {{path/to/file}}
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
