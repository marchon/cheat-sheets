# gunicorn

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gunicorn/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
hardhat
,
tsort
,
electrum
,
ned
,
cabal
.
gunicorn
Python WSGI HTTP Server.
More information:
https://gunicorn.org/
.
Run Python web app:
gunicorn {{import.path:app_object}}
Listen on port 8080 on localhost:
gunicorn --bind {{localhost}}:{{8080}} {{import.path:app_object}}
Turn on live reload:
gunicorn --reload {{import.path:app_object}}
Use 4 worker processes for handling requests:
gunicorn --workers {{4}} {{import.path:app_object}}
Use 4 worker threads for handling requests:
gunicorn --threads {{4}} {{import.path:app_object}}
Run app over HTTPS:
gunicorn --certfile {{cert.pem}} --keyfile {{key.pem}} {{import.path:app_object}}
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
