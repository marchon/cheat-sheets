# bootctl

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/bootctl/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mosquitto
,
ex
,
llc
,
wait
,
jpegoptim
.
bootctl
Control EFI firmware boot settings and manage boot loader.
More information:
https://manned.org/bootctl
.
Show information about the system firmware and the bootloaders:
sudo bootctl status
Set a flag to boot into the system firmware on the next boot (similar to
sudo systemctl reboot --firmware-setup
):
sudo bootctl reboot-to-firmware true
Specify the path to the EFI system partition (defaults to
/efi/
,
/boot/
or
/boot/efi
):
sudo bootctl --esp-path={{/path/to/efi_system_partition/}}
Show all available bootloader entries:
sudo bootctl list
Install
systemd-boot
into the EFI system partition:
sudo bootctl install
Remove all installed versions of
systemd-boot
from the EFI system partition:
sudo bootctl remove
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
