# Rewrite engine

Cloned from https://en.wikipedia.org/wiki/Rewrite_engine.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 265738.

In web applications, a rewrite engine is a software component that performs rewriting on URLs (Uniform Resource Locators), modifying their appearance. This modification is called URL rewriting. It is a way of implementing URL mapping or routing within a web application. The engine is typically a component of a web server or web application framework. Rewritten URLs (sometimes known as short, pretty or fancy URLs, search engine friendly - SEF URLs, or slugs) are used to provide shorter and more relevant-looking links to web pages. The technique adds a layer of abstraction between the files used to generate a web page and the URL that is presented to the outside world.


== Usage ==

Web sites with dynamic content can use URLs that generate pages from the server using query string parameters. These are often rewritten to resemble URLs for static pages on a site with a subdirectory hierarchy. For example, the URL to a wiki page with title Rewrite_engine might be:

http://example.com/w/index.php?title=Rewrite_engine

but can be rewritten as:

http://example.com/wiki/Rewrite_engine

A blog might have a URL that encodes the dates of each entry:

http://www.example.com/Blog/Posts.php?Year=2006&Month=12&Day=19

It can be altered like this:

http://www.example.com/Blog/2006/12/19/

which also allows the user to change the URL to see all postings available in December, simply by removing the text encoding the day '19', as though navigating "up" a directory:

http://www.example.com/Blog/2006/12/

A site can pass specialized terms from the URL to its search engine as a search term. This would allow users to search directly from their browser. For example, the URL as entered into the browser's location bar:

http://example.com/search term

will be URL-encoded by the browser before it makes the HTTP request. The server could rewrite this to:

http://example.com/search.php?q=search%20term


== Benefits and drawbacks ==

There are several benefits to using URL rewriting:

The links are "cleaner" and more descriptive, improving their "friendliness" to both users and search engines.
They prevent undesired "inline linking", which can waste bandwidth.
The site can continue to use the same URLs even if the underlying technology used to serve them is changed (for example, switching to a new blogging engine).
There can, however be drawbacks as well; if a user wants to modify a URL to retrieve new data, URL rewriting may hinder the construction of custom queries due to the lack of named variables. For example, it may be difficult to determine the date from the following format:

http://www.example.com/Blog/06/04/02/

In this case, the original query string was more useful, since the query variables indicated month and day:

http://www.example.com/Blog/Posts.php?Year=06&Month=04&Day=02


== Web frameworks ==
Many web frameworks include URL rewriting, either directly or through extension modules.

Apache HTTP Server has URL rewriting provided by the mod_rewrite module.
URL Rewrite is available as an extension to Microsoft IIS.
Ruby on Rails has built-in URL rewriting via Routes.
Jakarta Servlet has extendable URL rewriting via the OCPsoft URLRewriteFilter and Tuckey UrlRewriteFilter.
Jakarta Faces has simplified URL rewriting via the PrettyFaces: URLRewriteFilter.
Django uses a regular-expressions-based system. This is not strictly URL rewriting since there is no script to 'rewrite' to, nor even a directory structure; but it provides the full flexibility of URL rewriting.
Java Stripes Framework has had integrated functionality since version 1.5.
Many Perl frameworks, such as Mojolicious and Catalyst, have this feature.
CodeIgniter has URL rewriting provided.
lighttpd has a mod_rewrite module.
nginx has a rewrite module. For example, a multi-link multi-variable page generation from a URI like /f101,n61,o56,d/ifconfig is possible, where multiple individual parts like f101 get expanded with the help of regular expressions into variables to signify FreeBSD 10.1-RELEASE and so forth.
Hiawatha HTTP server has a URL Toolkit which supports URL rewriting.
Cherokee HTTP server supports regular expressions of URL rewriting and redirections.
From a software development perspective, URL rewriting can aid in code modularization and control flow,  making it a useful feature of modern web frameworks.


== See also ==
Application Delivery Controller
aiScaler Traffic Manager
.htaccess
Apache HTTP Server
Content negotiation
HTTP
Internet Information Server
Permalink
Zeus Web Server


== Notes ==


== External links ==
Apache mod_rewrite
