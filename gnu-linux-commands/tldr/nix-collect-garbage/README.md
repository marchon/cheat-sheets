# nix-collect-garbage

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/nix-collect-garbage/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
glab pipeline
,
fortune
,
lpass
.
nix-collect-garbage
Delete unused and unreachable nix store paths.
Generations can be listed using
nix-env --list-generations
.
More information:
https://nixos.org/releases/nix/latest/manual/#sec-nix-collect-garbage
.
Delete all store paths unused by current generations of each profile:
sudo nix-collect-garbage --delete-old
Simulate the deletion of old store paths:
sudo nix-collect-garbage --delete-old --dry-run
Delete all store paths older than 30 days:
sudo nix-collect-garbage --delete-older-than {{30d}}
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
