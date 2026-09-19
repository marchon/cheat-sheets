# svgr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/svgr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
cups config
,
adguardhome
,
mc
.
svgr
Transform SVGs into React components.
More information:
https://react-svgr.com
.
Transform a SVG file into a React component to stdout:
svgr -- {{path/to/file.svg}}
Transform a SVG file into a React component using TypeScript to stdout:
svgr --typescript -- {{path/to/file.svg}}
Transform a SVG file into a React component using JSX transform to stdout:
svgr --jsx-runtime automatic -- {{path/to/file.svg}}
Transform all SVG files from a directory to React components into a specific directory:
svgr --out-dir {{path/to/output_directory}} {{path/to/input_directory}}
Transform all SVG files from a directory to React components into a specific directory skipping already transformed files:
svgr --out-dir {{path/to/output_directory}} --ignore-existing {{path/to/input_directory}}
Transform all SVG files from a directory to React components into a specific directory using a specific case for filenames:
svgr --out-dir {{path/to/output_directory}} --filename-case {{camel|kebab|pascal}} {{path/to/input_directory}}
Transform all SVG files from a directory to React components into a specific directory without generating an index file:
svgr --out-dir {{path/to/output_directory}} --no-index {{path/to/input_directory}}
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
