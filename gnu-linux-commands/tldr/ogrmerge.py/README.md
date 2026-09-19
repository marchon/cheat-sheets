# ogrmerge.py

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ogrmerge.py/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
clamdscan
,
openssl x509
,
nth
.
ogrmerge.py
Merge several vector datasets into a single one.
More information:
https://gdal.org/programs/ogrmerge.html
.
Create a GeoPackage with a layer for each input Shapefile:
ogrmerge.py -f {{GPKG}} -o {{path/to/output.gpkg}} {{path/to/input1.shp path/to/input2.shp ...}}
Create a virtual datasource (VRT) with a layer for each input GeoJSON:
ogrmerge.py -f {{VRT}} -o {{path/to/output.vrt}} {{path/to/input1.geojson path/to/input2.geojson ...}}
Concatenate two vector datasets and store source name of dataset in attribute 'source_name':
ogrmerge.py -single -f {{GeoJSON}} -o {{path/to/output.geojson}} -src_layer_field_name country {{source_name}} {{path/to/input1.shp path/to/input2.shp ...}}
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
