# babel

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/babel/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git ignore io
,
virsh pool undefine
.
babel
A transpiler which converts code from JavaScript ES6/ES7 syntax to ES5 syntax.
More information:
https://babeljs.io/
.
Transpile a specified input file and output to stdout:
babel {{path/to/file}}
Transpile a specified input file and output to a specific file:
babel {{path/to/input_file}} --out-file {{path/to/output_file}}
Transpile the input file every time it is changed:
babel {{path/to/input_file}} --watch
Transpile a whole directory of files:
babel {{path/to/input_directory}}
Ignore specified comma-separated files in a directory:
babel {{path/to/input_directory}} --ignore {{ignored_files}}
Transpile and output as minified JavaScript:
babel {{path/to/input_file}} --minified
Choose a set of presets for output formatting:
babel {{path/to/input_file}} --presets {{presets}}
Output all available options:
babel --help
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
