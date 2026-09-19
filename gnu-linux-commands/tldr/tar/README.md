# tar

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/tar/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
p4
,
cargo clippy
,
gdal2tiles.py
.
tar
Archiving utility.
Often combined with a compression method, such as gzip or bzip2.
More information:
https://www.gnu.org/software/tar
.
[c]reate an archive and write it to a [f]ile:
tar cf {{target.tar}} {{file1}} {{file2}} {{file3}}
[c]reate a g[z]ipped archive and write it to a [f]ile:
tar czf {{target.tar.gz}} {{file1}} {{file2}} {{file3}}
[c]reate a g[z]ipped archive from a directory using relative paths:
tar czf {{target.tar.gz}} --directory={{path/to/directory}} .
E[x]tract a (compressed) archive [f]ile into the current directory [v]erbosely:
tar xvf {{source.tar[.gz|.bz2|.xz]}}
E[x]tract a (compressed) archive [f]ile into the target directory:
tar xf {{source.tar[.gz|.bz2|.xz]}} --directory={{directory}}
[c]reate a compressed archive and write it to a [f]ile, using [a]rchive suffix to determine the compression program:
tar caf {{target.tar.xz}} {{file1}} {{file2}} {{file3}}
Lis[t] the contents of a tar [f]ile [v]erbosely:
tar tvf {{source.tar}}
E[x]tract files matching a pattern from an archive [f]ile:
tar xf {{source.tar}} --wildcards "{{*.html}}"
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
