# clang-tidy

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/clang-tidy/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git cat file
,
rscript
,
bat
,
grep
.
clang-tidy
An LLVM-based C/C++ linter to find style violations, bugs and security flaws through static analysis.
More information:
https://clang.llvm.org/extra/clang-tidy/
.
Run default checks on a source file:
clang-tidy {{path/to/file.cpp}}
Don't run any checks other than the
cppcoreguidelines
checks on a file:
clang-tidy {{path/to/file.cpp}} -checks={{-*,cppcoreguidelines-*}}
List all available checks:
clang-tidy -checks={{*}} -list-checks
Specify defines and includes as compilation options (after
--
):
clang-tidy {{path/to/file.cpp}} -- -I{{my_project/include}} -D{{definitions}}
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
