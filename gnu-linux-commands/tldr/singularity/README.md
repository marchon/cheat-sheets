# singularity

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/singularity/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
php yii
,
iex
,
jello
,
nix env
,
ember
.
singularity
Manage Singularity containers and images.
Download a remote image from Sylabs Cloud:
singularity pull --name {{image.sif}} {{library://godlovedc/funny/lolcow:latest}}
Rebuild a remote image using the latest Singularity image format:
singularity build {{image.sif}} {{docker://godlovedc/lolcow}}
Start a container from an image and get a shell inside it:
singularity shell {{image.sif}}
Start a container from an image and run a command:
singularity exec {{image.sif}} {{command}}
Start a container from an image and execute the internal runscript:
singularity run {{image.sif}}
Build a singularity image from a recipe file:
sudo singularity build {{image.sif}} {{recipe}}
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
