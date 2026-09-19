# ogr2ogr

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/ogr2ogr/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
zlib flate
,
virsh pool undefine
.
ogr2ogr
Convert geospatial vector data between file formats.
More information:
https://gdal.org/programs/ogr2ogr.html
.
Convert a Shapefile into a GeoPackage:
ogr2ogr -f GPKG {{path/to/output}}.gpkg {{path/to/input}}.shp
Reduce a GeoJSON to features matching a condition:
ogr2ogr -where '{{myProperty > 42}}' -f {{GeoJSON}} {{path/to/output.geojson}} {{path/to/input.geojson}}
Change coordinate reference system of a GeoPackage from
EPSG:4326
to
EPSG:3857
:
ogr2ogr -s_srs {{EPSG:4326}} -t_srs {{EPSG:3857}} -f GPKG {{path/to/output}}.gpkg {{path/to/input}}.gpkg
Convert a CSV file into a GeoPackage, specifying the names of the coordinate columns and assigning a coordinate reference system:
ogr2ogr -f GPKG {{path/to/output}}.gpkg {{path/to/input}}.csv -oo X_POSSIBLE_NAMES={{longitude}} -oo Y_POSSIBLE_NAMES={{latitude}} -a_srs {{EPSG:4326}}
Load a GeoPackage into a PostGIS database:
ogr2ogr -f PostgreSQL PG:dbname="{{database_name}}" {{path/to/input}}.gpkg
Clip layers of a GeoPackage file to the given bounding box:
ogr2ogr -spat {{min_x}} {{min_y}} {{max_x}} {{max_y}} -f GPKG {{path/to/output}}.gpkg {{path/to/input}}.gpkg
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
