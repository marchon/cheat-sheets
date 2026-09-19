# elm

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/elm/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
acme.sh dns
,
clojure
,
phpcbf
.
elm
Compile and run Elm source files.
More information:
https://elm-lang.org
.
Initialize an Elm project, generates an elm.json file:
elm init
Start interactive Elm shell:
elm repl
Compile an Elm file, output the result to an
index.html
file:
elm make {{source}}
Compile an Elm file, output the result to a JavaScript file:
elm make {{source}} --output={{destination}}.js
Start local web server that compiles Elm files on page load:
elm reactor
Install Elm package from https://package.elm-lang.org:
elm install {{author}}/{{package}}
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
