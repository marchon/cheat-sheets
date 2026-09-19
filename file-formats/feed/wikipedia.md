# Web feed

Cloned from https://en.wikipedia.org/wiki/Web_feed.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 717016.

On the World Wide Web, a web feed (or news feed) is a data format used for providing users with frequently updated content. Content distributors syndicate a web feed, thereby allowing users to subscribe a channel to it by adding the feed resource address to a news aggregator client (also called a feed reader or a news reader). Users typically subscribe to a feed by manually entering the URL of a feed or clicking a link in a web browser or by dragging the link from the web browser to the aggregator, thus "RSS and Atom files provide news updates from a website in a simple form for your computer." 
The kinds of content delivered by a web feed are typically HTML (webpage content) or links to webpages and other kinds of digital media. Often, when websites provide web feeds to notify users of content updates, they only include summaries in the web feed rather than the full content itself. Many news websites, weblogs, schools and podcasters operate web feeds. As web feeds are designed to be machine-readable rather than human-readable they can also be used to automatically transfer information from one website to another without any human intervention.


== Technical definition ==
A web feed is a document (often XML-based) whose discrete content items include web links to the source of the content. News websites and blogs are common sources for web feeds, but feeds are also used to deliver structured information ranging from weather data to search results. 
Common web feed formats are:

RSS (1999–2009)
Atom (2005–2007)
JSON Feed (2017–2020)
Although RSS formats have evolved since March 1999, the RSS icon ("") first gained widespread use between 2005 and 2006. The feed icon indicates that a web feed is available. 
The original icon was created by Stephen Horlander, a designer at Mozilla. 
With the prevalence of JSON in Web APIs, a further format, JSON Feed, was defined in 2017.


== History ==
Dave Winer published a modified version of the RSS 0.91 specification on the UserLand website, covering how it was being used in his company's products and claimed copyright to the document. A few months later, UserLand filed a U.S. trademark registration for RSS, but failed to respond to a USPTO trademark examiner's request and the request was rejected in December 2001.
The RSS-DEV Working Group, a project whose members included Guha and representatives of O'Reilly Media and Moreover, produced RSS 1.0 in December 2000. This new version, which reclaimed the name RDF Site Summary from RSS 0.9, reintroduced support for RDF and added XML namespaces support, adopting elements from standard metadata vocabularies such as Dublin Core.
In December 2000, Winer released RSS 0.92
a minor set of changes aside from the introduction of the enclosure element, which permitted audio files to be carried in RSS feeds and helped spark podcasting. He also released drafts of RSS 0.93 and RSS 0.94 that were subsequently withdrawn.
In September 2002, Winer released a major new version of the format, RSS 2.0, that redubbed its initials Really Simple Syndication. RSS 2.0 removed the type attribute added in the RSS 0.94 draft and added support for namespaces.
Because neither Winer nor the RSS-DEV Working Group had Netscape's involvement, they could not make an official claim on the RSS name or format. This has fueled ongoing controversy in the syndication development community as to which entity was the proper publisher of RSS.
One product of that contentious debate was the creation of an alternative syndication format, Atom, that began in June 2003. The Atom syndication format, whose creation was in part motivated by a desire to get a clean start free of the issues surrounding RSS, has been adopted as RFC 4287.
In July 2003, Winer and UserLand Software assigned the copyright of the RSS 2.0 specification to Harvard's Berkman Center for Internet & Society, where he had just begun a term as a visiting fellow. At the same time, Winer launched the RSS Advisory Board with Brent Simmons and Jon Udell, a group whose purpose was to maintain and publish the specification and answer questions about the format.
In December 2005, the Microsoft Internet Explorer team and
Outlook team announced on their blogs that they were adopting the feed icon first used in the Mozilla Firefox browser , created by Stephen Horlander, a Mozilla Designer. A few months later, Opera Software followed suit. This effectively made the orange square with white radio waves the industry standard for RSS and Atom feeds, replacing the large variety of icons and text that had been used previously to identify syndication data.
In January 2006, Rogers Cadenhead relaunched the RSS Advisory Board without Dave Winer's participation, with a stated desire to continue the development of the RSS format and resolve ambiguities. In June 2007, the board revised their version of the specification to confirm that namespaces may extend core elements with namespace attributes, as Microsoft has done in Internet Explorer 7. According to their view, a difference of interpretation left publishers unsure of whether this was permitted or forbidden.


== Comparison to email subscriptions ==
Web feeds have some advantages compared to receiving frequently published content via an email:

Users do not disclose their email address when subscribing to a feed and so are not increasing their exposure to threats associated with email: spam, viruses, phishing and identity theft.
Users do not have to send an unsubscribe request to stop receiving news. They simply remove the feed from their aggregator.
The feed items are automatically sorted in that each feed URL has its own sets of entries (unlike an email box where messages must be sorted by user-defined rules and pattern matching).


== RSS compared with Atom ==
Both RSS and Atom are widely supported and are compatible with all major consumer feed readers. RSS gained wider use because of early feed reader support. Technically, Atom has several advantages: less restrictive licensing, IANA-registered MIME type, XML namespace, URI support, RELAX NG support.
The following table shows RSS elements alongside Atom elements where they are equivalent.
Note: the asterisk character (*) indicates that an element must be provided (Atom elements "author" and "link" are only required under certain conditions).


== See also ==
See Wikipedia:Syndication on how various aspects of Wikipedia can be monitored with RSS or Atom feeds.
Web syndication
feed: URI scheme
Share icon
OPML
Podcast
Feed reader
WebSub
JSON Feed


== References ==


== External links ==

Pilgrim, Mark (December 18, 2002). "What is RSS?".
Shea, Dave (May 19, 2004). "What is RSS/XML/Atom/Syndication?". Archived from the original on November 2, 2010. Retrieved February 16, 2006.
