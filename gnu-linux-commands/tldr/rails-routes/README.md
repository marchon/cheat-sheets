# rails-routes

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rails-routes/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
borg
,
cupsd
,
az
,
docker swarm
,
pamixer
.
rails routes
List routes in a Rails application.
More information:
https://guides.rubyonrails.org/routing.html
.
List all routes:
rails routes
List all routes in an expanded format:
rails routes --expanded
List routes partially matching URL helper method name, HTTP verb, or URL path:
rails routes -g {{posts_path|GET|/posts}}
List routes that map to a specified controller:
rails routes -c {{posts|Posts|Blogs::PostsController}}
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
