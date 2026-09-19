# Ajax (programming)

Cloned from https://en.wikipedia.org/wiki/Ajax_(programming).

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 1610950.

Asynchronous JavaScript and XML, usually referred to as Ajax (sometimes capitalized AJAX, ) is a set of web development techniques that uses various asynchronous web technologies on the client-side to create web applications. With Ajax, web applications can send and retrieve data from a server asynchronously (in the background) without interfering with the display and behavior of the existing page. By decoupling the data interchange layer from the presentation layer, Ajax allows web pages and, by extension, web applications, to change content dynamically without the need to reload the entire page. In practice, modern implementations commonly return JSON instead of XML; and can return anything, e.g. HTML when used with htmx.
Ajax is not a technology, but rather a programming pattern. The webpage can be modified by JavaScript to dynamically display (and allow the user to interact with) retrieved information without refreshing the page. The built-in XMLHttpRequest object can be used to execute Ajax requests on webpages, and the built-in fetch() function is a newer alternative to XMLHttpRequest that can also be used to perform Ajax.


== History ==
In the early-to-mid 1990s, most websites were based on complete HTML pages. Each user action required a complete new page to be loaded from the server. This process was inefficient, as reflected by the user experience: all page content disappeared, then the new page appeared. Each time the browser reloaded a page because of a partial change, all the content had to be re-sent, even though only some of the information had changed. This placed additional load on the server and made bandwidth a limiting factor in performance.
The foundations of Ajax originate back in 1996 with the introduction of JavaScript 1. Developers quickly discovered that any HTML element which accepted a "src" attribute could be used to fetch remote data. By changing the src of a hidden frame, a developer could fetch remote data, process or display it without a page refresh. The remote data could be a string, JavaScript code, XML or a partial HTML page generated on the server. The same could be done with <img> and <embed> tags, but many developers were alarmed at the concept of an executable GIF and preferred to use the hidden <iframe>. This technique was used for both Netscape Navigator and Internet Explorer, the two main browsers at the time, until developers discovered the XMLHTTP server object (MSXML 1.0) was included in Internet Explorer 4.
In 1996, the iframe tag was introduced by Internet Explorer to embed an web page inside another web page, with the embedded page loading asynchronously. In 1998, the Microsoft Outlook Web Access team developed the concept behind the XMLHttpRequest scripting object. It appeared as XMLHTTP in the second version of the MSXML library, which shipped with Internet Explorer 5.0 in March 1999.
The functionality of the Windows XMLHTTP ActiveX control in IE 5 was later implemented by Mozilla Firefox, Safari, Opera, Google Chrome, and other browsers as the XMLHttpRequest JavaScript object. Microsoft adopted the native XMLHttpRequest model as of Internet Explorer 7. Support for the ActiveX version remained in Internet Explorer and on "Internet Explorer mode" in Microsoft Edge. The utility of these background HTTP requests and asynchronous Web technologies remained fairly obscure until it started appearing in large scale online applications such as Outlook Web Access (2000) and Oddpost (2002).
Google made a wide deployment of standards-compliant, cross browser Ajax with Gmail (2004) and Google Maps (2005). In October 2004 Kayak.com's public beta release was among the first large-scale e-commerce uses of what their developers at that time called "the xml http thing". This increased interest in Ajax among web program developers.
The term Ajax was publicly used on 18 February 2005 by Jesse James Garrett in an article titled Ajax: A New Approach to Web Applications, based on techniques used on Google pages.
On 5 April 2006, the World Wide Web Consortium (W3C) released the first draft specification for the XMLHttpRequest object in an attempt to create an official Web standard.
In 2015, the Fetch standard was introduced as a modern alternative to the XMLHttpRequest object.
The last draft of the XMLHttpRequest object was published on 6 October 2016, and the XMLHttpRequest specification is now a living standard.


== Technologies ==

The term Ajax has come to represent a broad group of Web technologies that can be used to implement a Web application that communicates with a server in the background, without interfering with the current state of the page. In the article that coined the term Ajax, Jesse James Garrett explained that the following technologies are incorporated:

HTML (or XHTML) and CSS for presentation
The Document Object Model (DOM) for dynamic display of and interaction with data
JSON or XML for the interchange of data, and XSLT for XML manipulation
The XMLHttpRequest object for asynchronous communication
JavaScript to bring these technologies together
Since then, however, there have been a number of developments in the technologies used in an Ajax application, and in the definition of the term Ajax itself. XML is no longer required for data interchange and, therefore, XSLT is no longer required for the manipulation of data. JavaScript Object Notation (JSON) is often used as an alternative format for data interchange, although other formats such as preformatted HTML or plain text can also be used. A variety of popular JavaScript libraries, including jQuery, include abstractions to assist in executing Ajax requests.
XMLHttpRequest has been broadly supported across all major web browsers since Internet Explorer version 5, Firefox version 1.0, Opera version 7.6, and Safari version 1.2.


=== Fetch ===
Fetch is a JavaScript standard that was created to succeed XMLHttpRequest. According to Google Developers Documentation, "Fetch makes it easier to make web requests and handle responses than with the older XMLHttpRequest." Fetch relies on JavaScript Promises.
The Fetch specification differs from XMLHttpRequest in the following significant ways:

The Promise returned from fetch() won't reject on HTTP error status even if the response is an HTTP 404 or 500. Instead, as soon as the server responds with headers, the Promise will resolve normally (with the ok property of the response set to false if the response isn't in the range 200–299), and it will only reject on network failure or if anything prevented the request from completing.
fetch() won't send cross-origin cookies unless you set the credentials init option. (Since April 2018. The spec changed the default credentials policy to same-origin. Firefox changed since 61.0b13.)


== Examples ==


=== XMLHttpRequest example ===
An example of a simple Ajax request using the GET method. The client-side script is written in JavaScript with the XMLHttpRequest object, and the server-side script, which returns a simple, plain-text response, is written in PHP.
get-ajax-data.js:

send-ajax-data.php:


=== Fetch example ===
An example of the same client-side script using the Fetch function instead, with callback-style Promise syntax:


==== Async/await example ====
The same script using JavaScript's async/await syntax:


== See also ==


== References ==


== Further reading ==

Garrett, Jesse James (18 February 2005). Ajax: A New Approach to Web Applications (PDF). Retrieved 28 June 2025. — Article that coined the Ajax term and Q&A
