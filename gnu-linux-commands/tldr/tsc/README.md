# tsc

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tsc/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git reset
,
calibre server
,
xprop
.
tsc
TypeScript compiler.
More information:
https://www.typescriptlang.org/docs/handbook/compiler-options.html
.
Compile a TypeScript file
foobar.ts
into a JavaScript file
foobar.js
:
tsc {{foobar.ts}}
Compile a TypeScript file into JavaScript using a specific target syntax (default is
ES3
):
tsc --target {{ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT}} {{foobar.ts}}
Compile a TypeScript file into a JavaScript file with a custom name:
tsc --outFile {{output.js}} {{input.ts}}
Compile all
.ts
files of a TypeScript project defined in a
tsconfig.json
file:
tsc --build {{tsconfig.json}}
Run the compiler using command-line options and arguments fetched from a text file:
tsc @{{args.txt}}
Type-check multiple JavaScript files, and output only the errors:
tsc --allowJs --checkJs --noEmit {{src/**/*.js}}
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
