# cosign

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/cosign/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
gxl2gv
,
pushd
,
mupdf
,
openvpn
,
docker commit
.
cosign
Container Signing, Verification and Storage in an OCI registry.
More information:
https://github.com/sigstore/cosign
.
Generate a key-pair:
cosign generate-key-pair
Sign a container and store the signature in the registry:
cosign sign -key {{cosign.key}} {{image}}
Sign a container image with a key pair stored in a Kubernetes secret:
cosign sign -key k8s://{{namespace}}/{{key}} {{image}}
Sign a blob with a local key pair file:
cosign sign-blob --key {{cosign.key}} {{file}}
Verify a container against a public key:
cosign verify -key {{cosign.pub}} {{image}}
Verify images with a public key in a Dockerfile:
cosign dockerfile verify -key {{cosign.pub}} {{path/to/Dockerfile}}
Verify an image with a public key stored in a Kubernetes secret:
cosign verify -key k8s://{{namespace}}/{{key}} {{image}}
Copy a container image and its signatures:
cosign copy {{example.com/src:latest}} {{example.com/dest:latest}}
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
