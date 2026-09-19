# rails-generate

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rails-generate/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
awslogs
,
siege
,
jmap
,
git sizer
.
rails generate
Generate new Rails templates in an existing project.
More information:
https://guides.rubyonrails.org/command_line.html#bin-rails-generate
.
List all available generators:
rails generate
Generate a new model named Post with attributes title and body:
rails generate model {{Post}} {{title:string}} {{body:text}}
Generate a new controller named Posts with actions index, show, new and create:
rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}
Generate a new migration that adds a category attribute to an existing model called Post:
rails generate migration {{AddCategoryToPost}} {{category:string}}
Generate a scaffold for a model named Post, predefining the attributes title and body:
rails generate scaffold {{Post}} {{title:string}} {{body:text}}
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
