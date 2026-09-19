# uvicorn

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/uvicorn/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
rclone
,
steamcmd
,
opusenc
,
sed
.
uvicorn
Python ASGI HTTP Server, for asynchronous projects.
More information:
https://www.uvicorn.org/
.
Run Python web app:
uvicorn {{import.path:app_object}}
Listen on port 8080 on localhost:
uvicorn --host {{localhost}} --port {{8080}} {{import.path:app_object}}
Turn on live reload:
uvicorn --reload {{import.path:app_object}}
Use 4 worker processes for handling requests:
uvicorn --workers {{4}} {{import.path:app_object}}
Run app over HTTPS:
uvicorn --ssl-certfile {{cert.pem}} --ssl-keyfile {{key.pem}} {{import.path:app_object}}
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
