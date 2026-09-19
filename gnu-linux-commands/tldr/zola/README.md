# zola

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/zola/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mm2gv
,
bssh
,
git cp
,
glances
,
git send email
.
zola
A static site generator in a single binary with everything built-in.
More information:
https://www.getzola.org/documentation/getting-started/cli-usage/
.
Create the directory structure used by Zola at the given directory:
zola init {{my_site}}
Build the whole site in the
public
directory after deleting it:
zola build
Build the whole site into a different directory:
zola build --output-dir {{path/to/output_directory/}}
Build and serve the site using a local server (default is
127.0.0.1:1111
):
zola serve
Build all pages just like the build command would, but without writing any of the results to disk:
zola check
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
