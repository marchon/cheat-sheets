# nix-env

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nix-env/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
arduino
,
dotnet ef
,
betty
,
gnuplot
.
nix-env
Manipulate or query Nix user environments.
More information:
https://nixos.org/manual/nix/stable/#sec-nix-env
.
List all installed packages:
nix-env -q
Query installed packages:
nix-env -q {{search_term}}
Query available packages:
nix-env -qa {{search_term}}
Install package:
nix-env -iA nixpkgs.{{pkg_name}}
Install a package from a URL:
nix-env -i {{pkg_name}} --file {{example.com}}
Uninstall package:
nix-env -e {{pkg_name}}
Upgrade one package:
nix-env -u {{pkg_name}}
Upgrade all packages:
nix-env -u
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
