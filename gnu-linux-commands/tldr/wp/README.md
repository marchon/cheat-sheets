# wp

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/wp/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
sonar scanner
,
dua
,
gh issue create
.
wp
The official command-line interface to manage WordPress instances.
More information:
https://wp-cli.org/
.
Print information about the operating system, shell, PHP, and WP-CLI (
wp
) installation:
wp --info
Update WP-CLI:
wp cli update
Download a fresh WordPress installation to current directory, optionally specifying the locale:
wp core download --locale={{locale}}
Create basic
wpconfig
file (assuming database on
localhost
):
wp config create --dbname={{dbname}} --dbuser={{dbuser}} --dbpass={{dbpass}}
Install and activate a WordPress plugin:
wp plugin install {{plugin}} --activate
Replace all instances of a string in the database:
wp search-replace {{old_string}} {{new_string}}
Import the contents of a WordPress Extended RSS (WXR) file:
wp import {{path/to/file.xml}}
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
