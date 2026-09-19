# montage

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/montage/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
printf
,
whereis
,
pyenv virtualenv
.
montage
ImageMagick image montage tool.
Tiles images into a customisable grid.
More information:
https://imagemagick.org/script/montage.php
.
Tile images into a grid, automatically resizing images larger than the grid cell size:
montage {{image1.png}} {{image2.jpg}} {{imageN.png}} montage.jpg
Tile images into a grid, automatically calculating the grid cell size from the largest image:
montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry +0+0 montage.jpg
Set the grid cell size and resize images to fit it before tiling:
montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry 640x480+0+0 montage.jpg
Limit the number of rows and columns in the grid, causing input images to overflow into multiple output montages:
montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry +0+0 -tile 2x3 montage_%d.jpg
Resize and crop images to fill their grid cells before tiling:
montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry +0+0 -resize 640x480^ -gravity center -crop 640x480+0+0 montage.jpg
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
