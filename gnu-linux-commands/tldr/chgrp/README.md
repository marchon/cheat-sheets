# chgrp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/chgrp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virt sparsify
,
john
,
glab mr create
.
chgrp
Change group ownership of files and directories.
More information:
https://www.gnu.org/software/coreutils/chgrp
.
Change the owner group of a file/directory:
chgrp {{group}} {{path/to/file_or_directory}}
Recursively change the owner group of a directory and its contents:
chgrp -R {{group}} {{path/to/directory}}
Change the owner group of a symbolic link:
chgrp -h {{group}} {{path/to/symlink}}
Change the owner group of a file/directory to match a reference file:
chgrp --reference={{path/to/reference_file}} {{path/to/file_or_directory}}
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
