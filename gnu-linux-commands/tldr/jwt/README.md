# jwt

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/jwt/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
awk
,
surge
,
git apply
,
pueue status
.
jwt
A command-line tool to work with JSON Web Tokens (JWTs).
Encryption algorithms available are HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384.
More information:
https://github.com/mike-engel/jwt-cli
.
Decode a JWT:
jwt decode {{jwt_string}}
Decode a JWT as a JSON string:
jwt decode -j {{jwt_string}}
Encode a JSON string to a JWT:
jwt encode --alg {{HS256}} --secret {{1234567890}} '{{json_string}}'
Encode key pair payload to JWT:
jwt encode --alg {{HS256}} --secret {{1234567890}} -P key=value
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
