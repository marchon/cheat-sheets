# Atom (web standard)

Cloned from https://en.wikipedia.org/wiki/Atom_(web_standard).

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 509078.

The name Atom applies to a pair of related Web standards.  The Atom Syndication Format is an XML language used for web feeds, while the Atom Publishing Protocol (AtomPub or APP) is a simple HTTP-based protocol for creating and updating web resources.
Web feeds allow software programs to check for updates published on a website.  To provide a web feed, the site owner may use specialized software (such as a content management system) that publishes a list (or "feed") of recent articles or content in a standardized, machine-readable format.  The feed can then be downloaded by programs that use it, like websites that syndicate content from the feed, or by feed reader programs that allow internet users to subscribe to feeds and view their content.
A feed contains entries, which may be headlines, full-text articles, excerpts, summaries or links to content on a website  along with various metadata.
The Atom format was developed as an alternative to RSS. Ben Trott, an advocate of the new format that became Atom, believed that RSS had limitations and flaws—such as lack of on-going innovation and its necessity to remain backward compatible—and that there were advantages to a fresh design.
Proponents of the new format formed the IETF Atom Publishing Format and Protocol Workgroup. The Atom Syndication Format was published as an IETF proposed standard in RFC 4287 (December 2005), and the Atom Publishing Protocol was published as RFC 5023 (October 2007).


== Usage ==
The blogging community uses web feeds to share recent entries' headlines, full text, and even attached multimedia files.  The providers allow other websites to incorporate a blog's "syndicated" headline or headline-and-short-summary feeds under various usage agreements.  As of 2016 people use Atom and other web-syndication formats for many purposes, including journalism, marketing, bug-reports, or any other activity involving periodic updates or publications.  Atom also provides a standard way to export an entire blog, or parts of it, for backup or for importing into other blogging systems.
It is common to find web feeds on major websites, as well as on many smaller ones. Some websites let people choose between RSS- or Atom-formatted web feeds; others offer only RSS or only Atom. In particular, many blog and wiki sites offer their web feeds in the Atom format.
A feed reader or "aggregator" program can be used to check feeds and to display new articles.  Client-side readers may also be designed as standalone programs or as extensions to existing programs like web browsers.
Web-based feed readers and news aggregators require no software installation and make the user's "feeds" available on any computer with web access. Some aggregators syndicate (combine) web feeds into new feeds, e.g., taking all football-related items from several sports feeds and providing a new football feed.


== Atom compared to RSS 2.0 ==
When Atom emerged as a format intended to rival or replace RSS, CNET described the motivation of its creators as follows: "Winer's opponents are seeking a new format that would clarify RSS ambiguities, consolidate its multiple versions, expand its capabilities, and fall under the auspices of a traditional standards organization."
A brief description of some of the ways Atom 1.0 differs from RSS 2.0 has been given by Tim Bray, who played a major role in the creation of Atom:


=== Date formats ===
The RSS 2.0 specification relies on the use of RFC 822 formatted timestamps to communicate information about when items in the feed were created and last updated. The Atom working group chose instead to use timestamps formatted according to the rules specified by RFC 3339 (which is a subset of ISO 8601; see Appendix A in RFC 3339 for differences).


=== Internationalization ===
While the RSS vocabulary has a mechanism to indicate a human language for the feed, there is no way to specify a language for individual items or text elements.  Atom, on the other hand, uses the standard xml:lang attribute to make it possible to specify a language context for every piece of human-readable content in the feed.
Atom also differs from RSS in that it supports the use of Internationalized Resource Identifiers, which allow links to resources and unique identifiers to contain characters outside the US ASCII character set.


=== Modularity ===
The elements of the RSS vocabulary are not generally reusable in other XML vocabularies. The Atom syntax was specifically designed to allow elements to be reused outside the context of an Atom feed document. For instance, it is not uncommon to find atom:link elements being used within RSS 2.0 feeds.


== Barriers to adoption ==
Despite the emergence of Atom as an IETF Proposed Standard and the decision by major companies such as Google to embrace Atom, use of the older and better-known RSS formats has continued. There are several reasons for this:

RSS 2.0 support for enclosures led directly to the development of podcasting. While many podcasting applications support the use of Atom 1.0, RSS 2.0 remains the preferred format. While iTunes previously supported Atom, it dropped support in 2023. and requires podcasts to be in RSS 2.0 format.
Many sites choose to publish their feeds in only a single format.  For example, CNN and The New York Times offer their web feeds only in RSS 2.0 format.
News articles about web syndication feeds have increasingly used the term "RSS" to refer generically to any of the several variants of the RSS format such as RSS 2.0 and RSS 1.0 as well as the Atom format.


== Development history ==


=== Background ===
Before the creation of Atom the primary method of web content syndication was the RSS family of formats.
Members of the community who felt there were significant deficiencies with this family of formats were unable to make changes directly to RSS 2.0 because the official specification document stated that it was purposely frozen to ensure its stability.


=== Initial work ===
In June 2003, Sam Ruby set up a wiki to discuss what makes "a well-formed log entry".  This initial posting acted as a rallying point. People quickly started using the wiki to discuss a new syndication format to address the shortcomings of RSS.  It also became clear that the new format could form the basis of a more robust replacement for blog editing protocols such as the Blogger API and LiveJournal XML-RPC Client/Server Protocol as well.
The project aimed to develop a web syndication format that was:

"100% vendor neutral,"
"implemented by everybody,"
"freely extensible by anybody, and"
"cleanly and thoroughly specified."
In short order, a project road map was built.  The effort quickly attracted more than 150 supporters, including David Sifry of Technorati, Mena Trott of Six Apart, Brad Fitzpatrick of LiveJournal, Jason Shellen of Blogger, Jeremy Zawodny of Yahoo, Timothy Appnel of the O'Reilly Network, Glenn Otis Brown of Creative Commons and Lawrence Lessig.  Other notables supporting Atom include Mark Pilgrim, Tim Bray, Aaron Swartz, Joi Ito, and Jack Park. Also, Dave Winer, the key figure behind RSS 2.0, gave tentative support to the new endeavor.
After this point, discussion became chaotic, due to the lack of a decision-making process. The project also lacked a name, tentatively using "Pie," "Echo," "Atom," and "Whatever" (PEAW) before settling on Atom.  After releasing a project snapshot known as Atom 0.2 in early July 2003, discussion was shifted off the wiki.


=== Atom 0.3 and adoption by Google ===
The discussion then moved to a newly set up mailing list.  The next and final snapshot during this phase was Atom 0.3, released in December 2003. This version gained widespread adoption in syndication tools, and in particular it was added to several Google-related services, such as Blogger, Google News, and Gmail.  Google's Data APIs (Beta) GData are based on Atom 1.0 and RSS 2.0.


=== Atom 1.0 and IETF standardization ===
In 2004, discussions began about moving the project to a standards body such as the World Wide Web Consortium or the Internet Engineering Task Force (IETF). The group eventually chose the IETF and the Atompub working group was formally set up in June 2004, finally giving the project a charter and process. The Atompub working group is co-chaired by Tim Bray (the co-editor of the XML specification) and Paul Hoffman. Initial development was focused on the syndication format.
The Atom Syndication Format was issued as a Proposed Standard in IETF RFC 4287 in December 2005. The co-editors were Mark Nottingham and Robert Sayre.  This document is known as atompub-format in IETF's terminology. The Atom Publishing Protocol was issued as a Proposed Standard in IETF RFC 5023 in October 2007. Two other drafts have not been standardized.


== Example of an Atom 1.0 feed ==
An example of a document in the Atom Syndication Format:


=== Including in HTML ===
The following tag should be placed into the head of an HTML document to provide a link to an Atom feed.


== RSS compared with Atom ==
Both RSS and Atom are widely supported and are compatible with all major consumer feed readers. RSS gained wider use because of early feed reader support. Technically, Atom has several advantages: less restrictive licensing, IANA-registered MIME type, XML namespace, URI support, RELAX NG support.
The following table shows RSS elements alongside Atom elements where they are equivalent.
Note: the asterisk character (*) indicates that an element must be provided (Atom elements "author" and "link" are only required under certain conditions).


== See also ==
hAtom – microformat for marking up (X)HTML so that Atom feeds can be derived from it
Micropub – W3C standard client–server protocol that uses HTTP to create, update, and delete; a more recent alternative to AtomPub except using OAuth for authentication instead of HTTP Basic Authentication
Channel Definition Format – an early feed format developed before Atom and RSS
Content Management Interoperability Services – provides an extension to AtomPub for content management
List of content syndication markup languages
Open Data Protocol – a set of extensions to AtomPub developed by Microsoft
OPML to exchange lists of Atom feeds between feed readers
SWORD (protocol)
Web syndication


== References ==


== External links ==
RFC 4287 – "The Atom Syndication Format"
RFC 5023 – "The Atom Publishing Protocol"
Comparison of RSS and Atom Web Feed Formats
Getting to know the Atom Publishing Protocol – IBM developerWorks article by James Snell
Ruby, Sam (16 June 2003). "Anatomy of a Well Formed Log Entry – the weblog post that started it all". Archived from the original on 17 February 2020.
