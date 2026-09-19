# ocamlfind

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ocamlfind/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
clang
,
apm
,
kubectl get
,
zipgrep
.
ocamlfind
The findlib package manager for OCaml.
Simplifies linking executables with external libraries.
More information:
http://projects.camlcity.org/projects/findlib.html
.
Compile a source file to a native binary and link with packages:
ocamlfind ocamlopt -package {{package1}},{{package2}} -linkpkg -o {{executable}} {{source_file.ml}}
Compile a source file to a bytecode binary and link with packages:
ocamlfind ocamlc -package {{package1}},{{package2}} -linkpkg -o {{executable}} {{source_file.ml}}
Cross-compile for a different platform:
ocamlfind -toolchain {{cross-toolchain}} ocamlopt -o {{executable}} {{source_file.ml}}
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
