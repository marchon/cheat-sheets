# composer

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/composer/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
git locked
,
git rename remote
.
composer
A package-based dependency manager for PHP projects.
More information:
https://getcomposer.org/
.
Interactively create a
composer.json
file:
composer init
Add a package as a dependency for this project, adding it to
composer.json
:
composer require {{user/package_name}}
Install all the dependencies in this project's
composer.json
and create
composer.lock
:
composer install
Uninstall a package from this project, removing it as a dependency from
composer.json
:
composer remove {{user/package_name}}
Update all the dependencies in this project's
composer.json
and note versions in
composer.lock
file:
composer update
Update composer lock only after updating
composer.json
manually:
composer update --lock
Learn more about why a dependency can't be installed:
composer why-not {{user/package_name}}
Update composer to its latest version:
composer self-update
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
