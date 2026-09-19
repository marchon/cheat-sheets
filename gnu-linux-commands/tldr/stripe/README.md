# stripe

TLDR page cloned from https://www.cheat-sheets.org/project/tldr/command/stripe/.

Upstream tldr pages are CC BY 4.0 (https://github.com/tldr-pages/tldr).

TLDR
Search
JavaScript must be enabled for this application.
Enter a command. For example:
mkvmerge
,
pueue switch
,
lsof
.
stripe
Interact with a Stripe account.
More information:
https://github.com/stripe/stripe-cli
.
Follow the logs of activity on the account:
stripe logs tail
Listen for events, filtering on events with the name
charge.succeeded
and forwarding them to localhost:3000/events:
stripe listen --events="{{charge.succeeded}}" --forward-to="{{localhost:3000/events}}"
Send a test webhook event:
stripe trigger {{charge.succeeded}}
Create a customer:
stripe customers create --email="{{test@example.com}}" --name="{{Jenny Rosen}}"
Print to JSON:
stripe listen --print-json
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
