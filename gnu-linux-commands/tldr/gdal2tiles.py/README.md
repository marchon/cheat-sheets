# gdal2tiles.py

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/gdal2tiles.py/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
virsh pool list
,
git config
.
gdal2tiles.py
Generate TMS or XYZ tiles for a raster dataset.
More information:
https://gdal.org/programs/gdal2tiles.html
.
Generate TMS tiles for the zoom levels 2-5 of a raster dataset:
gdal2tiles.py --zoom={{2-5}} {{path/to/input.tif}} {{path/to/output_directory}}
Generate XYZ tiles for the zoom levels 2-5 of a raster dataset:
gdal2tiles.py --zoom={{2-5}} --xyz {{path/to/input.tif}} {{path/to/output_directory}}
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
