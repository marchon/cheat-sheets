# rails-db

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/rails-db/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
npm why
,
srm
,
xgettext
,
pueue shutdown
.
rails db
Various database-related subcommands for Ruby on Rails.
More information:
https://guides.rubyonrails.org/command_line.html
.
Create databases, load the schema, and initialize with seed data:
rails db:setup
Access the database console:
rails db
Create the databases defined in the current environment:
rails db:create
Destroy the databases defined in the current environment:
rails db:drop
Run pending migrations:
rails db:migrate
View the status of each migration file:
rails db:migrate:status
Rollback the last migration:
rails db:rollback
Fill the current database with data defined in
db/seeds.rb
:
rails db:seed
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
