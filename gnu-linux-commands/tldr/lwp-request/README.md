# lwp-request

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/lwp-request/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cpdf
,
mediainfo
,
netlify
,
gh
,
warp diag
.
lwp-request
Simple command-line HTTP client.
Built with libwww-perl.
More information:
https://metacpan.org/pod/lwp-request
.
Make a simple GET request:
lwp-request -m GET {{http://example.com/some/path}}
Upload a file with a POST request:
lwp-request -m POST {{http://example.com/some/path}} < {{path/to/file}}
Make a request with a custom user agent:
lwp-request -H 'User-Agent: {{user_agent}} -m {{METHOD}} {{http://example.com/some/path}}
Make a request with HTTP authentication:
lwp-request -C {{username}}:{{password}} -m {{METHOD}} {{http://example.com/some/path}}
Make a request and print request headers:
lwp-request -U -m {{METHOD}} {{http://example.com/some/path}}
Make a request and print response headers and status chain:
lwp-request -E -m {{METHOD}} {{http://example.com/some/path}}
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
