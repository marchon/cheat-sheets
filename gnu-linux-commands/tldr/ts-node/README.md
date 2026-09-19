# ts-node

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ts-node/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mpc
,
tlmgr update
,
screenfetch
.
ts-node
Run TypeScript code directly, without any compiling.
More information:
https://typestrong.org/ts-node
.
Execute a TypeScript file without compiling (
node
+
tsc
):
ts-node {{path/to/file.ts}}
Execute a TypeScript file without loading
tsconfig.json
:
ts-node --skip-project {{path/to/file.ts}}
Evaluate TypeScript code passed as a literal on the command-line:
ts-node --eval '{{console.log("Hello World")}}'
Execute a TypeScript file in script mode:
ts-node --script-mode {{path/to/file.ts}}
Transpile a TypeScript file to JavaScript without executing it:
ts-node --transpile-only {{path/to/file.ts}}
Display TS-Node help:
ts-node --help
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
