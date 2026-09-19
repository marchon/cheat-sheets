# nix-shell

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nix-shell/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git mergetool
,
xml unescape
.
nix-shell
Start an interactive shell based on a Nix expression.
More information:
https://nixos.org/manual/nix/stable/#sec-nix-shell
.
Start with nix expression in
shell.nix
or
default.nix
in the current directory:
nix-shell
Run shell command in non-interactive shell and exit:
nix-shell --run "{{command}} {{command_arguments}}"
Start with expression in
default.nix
in the current directory:
nix-shell {{default.nix}}
Start with packages loaded from nixpkgs:
nix-shell --packages {{package_name_1}} {{package_name_2}}
Start with packages loaded from specific nixpkgs revision:
nix-shell --packages {{package_names}} -I nixpkgs={{https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz}}
Evaluate rest of file in specific interpreter, for use in
#!-scripts
(see
https://nixos.org/manual/nix/stable/#use-as-a-interpreter
):
nix-shell -i {{interpreter}} --packages {{package_names}}
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
