# Adobe ColdFusion

Cloned from https://en.wikipedia.org/wiki/Adobe_ColdFusion.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 374636.

Adobe ColdFusion is a commercial rapid web-application development computing platform created by J. J. Allaire in 1995. (The programming language used with that platform is also commonly called ColdFusion, though is more accurately known as CFML.) ColdFusion was originally designed to make it easier to connect simple HTML pages to a database. By version 2 (1996) it had become a full platform that included an IDE in addition to a full scripting language.


== Overview ==
One of the distinguishing features of ColdFusion is its associated scripting language, ColdFusion Markup Language (CFML). CFML compares to the scripting components of ASP, JSP, and PHP in purpose and features, but its tag syntax more closely resembles HTML, while its script syntax resembles JavaScript. ColdFusion is often used synonymously with CFML, but there are additional CFML application servers besides ColdFusion, and ColdFusion supports programming languages other than CFML, such as server-side Actionscript and embedded scripts that can be written in a JavaScript-like language known as CFScript.
Originally a product of Allaire and released on July 2, 1995, ColdFusion was developed by brothers Joseph J. Allaire and Jeremy Allaire. In 2001 Allaire was acquired by Macromedia, which in turn was acquired by Adobe Systems Inc in 2005.
ColdFusion is most often used for data-driven websites or intranets, but can also be used to generate remote services such as REST services, WebSockets, SOAP web services or Flash remoting. It is especially well-suited as the server-side technology to the client-side ajax.
ColdFusion can also handle asynchronous events such as SMS and instant messaging via its gateway interface, available in ColdFusion MX 7 Enterprise Edition.


=== Main features ===
ColdFusion provides a number of additional features out of the box. Main features include:

Simplified database access
Client and server cache management
Client-side code generation, especially for form widgets and validation
Conversion from HTML to PDF
Data retrieval from common enterprise systems such as Active Directory, LDAP, SMTP, POP, HTTP, FTP, Microsoft Exchange Server and common data formats such as RSS and Atom
File indexing and searching service based on Apache Solr
GUI administration
Server, application, client, session, and request scopes
XML parsing, querying (XPath), validation and transformation (XSLT)
Server clustering
Task scheduling
Graphing and reporting
Simplified file manipulation including raster graphics (and CAPTCHA) and zip archives (introduction of video manipulation is planned in a future release)
Simplified web service implementation (with automated WSDL generation / transparent SOAP handling for both creating and consuming services - as an example, ASP.NET has no native equivalent for <CFINVOKE WEBSERVICE="http://host/tempconf.cfc?wsdl" METHOD="Celsius2Fahrenheit" TEMP="#tempc#" RETURNVARIABLE="tempf">)
Other implementations of CFML offer similar or enhanced functionality, such as running in a .NET environment or image manipulation.
The engine was written in C and featured, among other things, a built-in scripting language (CFScript), plugin modules written in Java, and a syntax very similar to HTML. The equivalent to an HTML element, a ColdFusion tag begins with the letters "CF" followed by a name that is indicative of what the tag is interpreted to, in HTML. E.g. <cfoutput> to begin the output of variables or other content.
In addition to CFScript and plugins (as described), CFStudio provided a design platform with a WYSIWYG display. In addition to ColdFusion, CFStudio also supports syntax in other languages popular for backend programming, such as Perl. In addition to making backend functionality easily available to the non-programmer, (version 4.0 and forward in particular) integrated easily with the Apache Web Server and with Internet Information Services.


=== Other features ===
All versions of ColdFusion prior to 6.0 were written using Microsoft Visual C++. This meant that ColdFusion was largely limited to running on Microsoft Windows, although Allaire did successfully port ColdFusion to Sun Solaris starting with version 3.1.
The Allaire company was sold to Macromedia, then Macromedia was sold to Adobe. Earlier versions were not as robust as the versions available from version 4.0 forward.
With the release of ColdFusion MX 6.0, the engine had been re-written in Java and supported its own runtime environment, which was easily replaced through its configuration options with the runtime environment from Sun. Version 6.1 included the ability to code and debug Macromedia Flash.


== Versions ==


=== Cold Fusion 3 ===
Version 3, released in June 1997, brought custom tags, cfsearch/cfindex/cfcollection based on the Verity search engine, the server scope, and template encoding (called then "encryption"). Version 3.1, released in Jan 1998, added RDS support as well as a port to the Sun Solaris operating system, while ColdFusion studio gained a live page preview and HTML syntax checker.


=== ColdFusion 4 ===
Released in Nov 1998, version 4 is when the name was changed from "Cold Fusion" to "ColdFusion" - possibly to distinguish it from Cold fusion theory. The release also added the initial implementation of cfscript, support for locking (cflock), transactions (cftransaction), hierarchical exception handling (cftry/cfcatch), sandbox security, as well as many new tags and functions, including cfstoredproc, cfcache, cfswitch, and more.


=== ColdFusion 4.5 ===
Version 4.5, released in Nov 1999, expanded the ability to access external system resources, including COM and CORBA, and added initial support for Java integration (including EJB's, Pojo's, servlets, and Java CFX's). IT also added the getmetricdata function (to access performance information), additional performance information in page debugging output, enhanced string conversion functions, and optional whitespace removal.


=== ColdFusion 5 ===
Version 5 was released in June 2001, adding enhanced query support, new reporting and charting features, user-defined functions, and improved admin tools. It was the last to be legacy coded for a specific platform, and the first release from Macromedia after their acquisition of Allaire Corporation, which had been announced January 16, 2001.


=== ColdFusion MX 6 ===
Prior to 2000, Edwin Smith, an Allaire architect on JRun and later the Flash Player, Tom Harwood and Clement Wong initiated a project codenamed "Neo". This project was later revealed as a ColdFusion Server re-written completely using Java. This made portability easier and provided a layer of security on the server, because it ran inside a Java Runtime Environment.
In June 2002 Macromedia released the version 6.0 product under a slightly different name, ColdFusion MX, allowing the product to be associated with both the Macromedia brand and its original branding. ColdFusion MX was completely rebuilt from the ground up and was based on the Java EE platform. ColdFusion MX was also designed to integrate well with Macromedia Flash using Flash Remoting.
With the release of ColdFusion MX, the CFML language API was released with an OOP interface.


=== ColdFusion MX 7 ===
With the release of ColdFusion 7.0 on February 7, 2005, the naming convention was amended, rendering the product name "Macromedia ColdFusion MX 7" (the codename for CFMX7 was "Blackstone"). CFMX 7 added Flash-based and XForms-based web forms, and a report builder that output in Adobe PDF as well as FlashPaper, RTF and Excel. The Adobe PDF output is also available as a wrapper to any HTML page, converting that page to a quality printable document. The enterprise edition also added Gateways. These provide interaction with non-HTTP request services such as IM Services, SMS, Directory Watchers, and an asynchronous execution. XML support was boosted in this version to include native schema checking.
ColdFusion MX 7.0.1 (codename "Merrimack") added support for Mac OS X, improvements to Flash forms, RTF support for CFReport, the new CFCPRoxy feature for Java/CFC integration, and more. ColdFusion MX 7.0.2 (codenamed "Mystic") included advanced features for working with Adobe Flex 2 as well as more improvements for the CF Report Builder.


=== Adobe ColdFusion 8 ===
On July 30, 2007, Adobe Systems released ColdFusion 8, dropping "MX" from its name. During beta testing the codename used was "Scorpio" (the eighth sign of the zodiac and the eighth iteration of ColdFusion as a commercial product). More than 14,000 developers worldwide were active in the beta process - many more testers than the 5,000 Adobe Systems originally expected. The ColdFusion development team consisted of developers based in Newton/Boston, Massachusetts and offshore in Bangalore, India.
Some of the new features are the CFPDFFORM tag, which enables integration with Adobe Acrobat forms, some image manipulation functions, Microsoft .NET integration, and the CFPRESENTATION tag, which allows the creation of dynamic presentations using Adobe Acrobat Connect, the Web-based collaboration solution formerly known as Macromedia Breeze. In addition, the ColdFusion Administrator for the Enterprise version ships with built-in server monitoring. ColdFusion 8 is available on several operating systems including Linux, Mac OS X and Windows Server 2003.
Other additions to ColdFusion 8 are built-in Ajax widgets, file archive manipulation (CFZIP), Microsoft Exchange server integration (CFEXCHANGE), image manipulation including automatic CAPTCHA generation (CFIMAGE), multi-threading, per-application settings, Atom and RSS feeds, reporting enhancements, stronger encryption libraries, array and structure improvements, improved database interaction, extensive performance improvements, PDF manipulation and merging capabilities (CFPDF), interactive debugging, embedded database support with Apache Derby, and a more ECMAScript compliant CFSCRIPT.
For development of ColdFusion applications, several tools are available: primarily Adobe Dreamweaver CS4, Macromedia HomeSite 5.x, CFEclipse, Eclipse and others. "Tag updaters" are available for these applications to update their support for the new ColdFusion 8 features.


=== Adobe ColdFusion 9 ===
ColdFusion 9 (Codenamed: Centaur) was released on October 5, 2009. New features for CF9 include:

Ability to code ColdFusion Components (CFCs) entirely in CFScript.
An explicit "local" scope that does not require local variables to be declared at the top of the function.
Implicit getters/setters for CFC.
Implicit constructors via method called "init" or method with same name as CFC.
New CFFinally tag for Exception handling syntax and CFContinue tag for Control flow.
Object–relational mapping (ORM) Database integration through Hibernate (Java).
Server.cfc file with onServerStart and onServerEnd methods.
Tighter integration with Adobe Flex and Adobe AIR.
Integration with key Microsoft products including Word, Excel, SharePoint, Exchange, and PowerPoint.
In Memory Management - or Virtual File System: an ability to treat content in memory as opposed to using the HDD.
Exposed as Services - an ability to access, securely, functions of the server externally.


=== Adobe ColdFusion 10 ===
ColdFusion 10 (Codenamed: Zeus) was released on May 15, 2012. New or improved features available in all editions (Standard, Enterprise, and Developer) include (but are not limited to):

Security enhancements
Hotfix installer and notification
Improved scheduler (based on a version of quartz)
Improved web services support (WSDL 2.0, SOAP 1.2)
Support for HTML5 web sockets
Tomcat integration
Support for RESTful web services
Language enhancements (closures, and more)
Search integration with Apache Solr
HTML5 video player and Adobe Flash Player
Flex and Adobe AIR lazy loading
XPath integration
HTML5 enhancements
Additional new or improved features in ColdFusion Enterprise or Developer editions include (but are not limited to):

Dynamic and interactive HTML5 charting
Improved and revamped scheduler (additional features over what is added in CF10 Standard)
Object relational mapping enhancements
The lists above were obtained from the Adobe web site pages describing "new features", as listed first in the links in the following list.
CF10 was originally referred to by the codename Zeus, after first being confirmed as coming by Adobe at Adobe MAX 2010, and during much of its prerelease period. It was also commonly referred to as "ColdFusion next" and "ColdFusion X" in blogs, on Twitter, etc., before Adobe finally confirmed it would be "ColdFusion 10". For much of 2010, ColdFusion Product Manager Adam Lehman toured the US setting up countless meetings with customers, developers, and user groups to formulate a master blueprint for the next feature set. In September 2010, he presented the plans to Adobe where they were given full support and approval by upper management.
The first public beta of ColdFusion 10 was released via Adobe Labs on 17 February 2012.


=== Adobe ColdFusion 11 ===
ColdFusion 11 (Codenamed: Splendor) was released on April 29, 2014.
New or improved features available in all editions (Standard, Enterprise, and Developer) include:

End-to-end mobile development
A new lightweight edition (ColdFusion Express)
Language enhancements
WebSocket enhancements
PDF generation enhancements
Security enhancements
Social enhancements
REST enhancements
Charting enhancements
Compression enhancements
ColdFusion 11 also removed many features previously identified simply as "deprecated" or no longer supported in earlier releases. For example, the CFLOG tag long offered date and time attributes which were deprecated (and redundant, as the date and time is always logged). As of CF11, their use would not cause the CFLOG tag to fail.


=== Adobe ColdFusion (2016 Release) ===
Adobe ColdFusion (2016 release), known generically as ColdFusion 2016 was released on February 16, 2016. During development, it was codenamed Raijin.
New or improved features available in all editions (Standard, Enterprise, and Developer) include:

Language enhancements
Command Line Interface (CLI)
PDF generation enhancements
Security enhancements
External session storage (Redis)
Swagger document generation
NTLM support
API Manager


=== Adobe ColdFusion (2018 Release) ===
Adobe ColdFusion (2018 release), known generically as ColdFusion 2018, was released on July 12, 2018. ColdFusion 2018 was codenamed Aether during prerelease.
As of March 2023, Adobe had released 16 updates for ColdFusion 2018.
New or improved features available in all editions (Standard, Enterprise, and Developer) include:

Language enhancements (including NULL, abstract classes and methods, covariants and finals, closures in tags, and more)
Asynchronous programming, using Futures
Command line REPL
Auto lockdown capability
Distributed cache support (Redis, memcached, JCS)
REST playground capability
Modernized Admin UI
Performance Monitoring Toolset


=== Adobe ColdFusion (2021 Release) ===
Adobe ColdFusion (2021 Release) was released on Nov 11th, 2020. ColdFusion 2021 was code named Project Stratus during pre-release.
New or improved features available in all editions (Standard, Enterprise, and Developer) include:

Lightweight installer
ColdFusion Package Manager
Cloud storage services
Messaging services
No-SQL database
Single sign-on
Core language changes
Performance Monitoring Tool set


=== Adobe ColdFusion (2023 Release) ===
Adobe released ColdFusion 2023 on May 17, 2023. ColdFusion 2023 was code named Project Fortuna during pre-release.
New features available are as follows: 

Google Cloud Platform (GCP) - Storage, Pub/Sub, FireStore
Central Configuration Server (CCS)
SSO CF Admin Integration (SAML/LDAP) including CF Admin API updates
JSON Web Tokens
Avro & Protocol Buffer Serialization
New PDF Engine
Library Updates (Java, Solr, Hibernate)
Native GraphQL Query support
Bug fixes


=== Adobe ColdFusion (2025 Release) ===
Adobe released ColdFusion 2025 on February 25, 2025. ColdFusion 2025 was referred to simply as "cfnext" during pre-release.


== Development roadmap ==
In Sep 2017, Adobe announced the roadmap anticipating releases in 2018 and 2020. Among the key features anticipated for the 2016 release were a new performance monitor, enhancements to asynchronous programming, revamped REST support, and enhancements to the API Manager, as well as support for CF2016 projected into 2024. As for the 2020 release, the features anticipated at that time (in 2017) were configurability (modularity) of CF application services, revamped scripting and object-oriented support, and further enhancements to the API Manager.


== Features ==


=== PDF generation ===
ColdFusion can generate PDF documents using standard HTML (i.e. no additional coding is needed to generate documents for print). CFML authors place HTML and CSS within a pair of cfdocument tags (or new in ColdFusion 11, cfhtmltopdf tags). The generated document can then either be saved to disk or sent to the client's browser. ColdFusion 8 introduced also the cfpdf tag to allow for control over PDF documents including PDF forms, and merging of PDFs. These tags however do not use Adobe's PDF engine but cfdocument uses a combination of the commercial JPedal Java PDF library and the free and open source Java library iText. The library used by cfhtmltopdf since cf11 has been an embedded WebKit IMPLEMENTATION. Since cf2023, Adobe has licensed PDFReactor to be the default engine underlying cfhtmltopdf.


=== ColdFusion Components (Objects) ===
ColdFusion was originally not an object-oriented programming language like PHP versions 3 and below. ColdFusion falls into the category of OO languages that do not support multiple inheritance (along with Java, Smalltalk, etc.). With the MX release (6+), ColdFusion introduced basic OO functionality with the component language construct which resembles classes in OO languages. Each component may contain any number of properties and methods. One component may also extend another (Inheritance). Components only support single inheritance. Object handling feature set and performance enhancing has occurred with subsequent releases. With the release of ColdFusion 8, Java-style interfaces are supported. ColdFusion components use the file extension cfc to differentiate them from ColdFusion templates (.cfm).


==== Remoting ====
Component methods may be made available as web services with no additional coding and configuration. All that is required is for a method's access to be declared 'remote'. ColdFusion automatically generates a WSDL at the URL for the component in this manner: http://path/to/components/Component.cfc?wsdl. Aside from SOAP, the services are offered in Flash Remoting binary format.
Methods which are declared remote may also be invoked via an HTTP GET or POST request. Consider the GET request as shown.

http://path/to/components/Component.cfc?method=search&query=your+query&mode=strict

This will invoke the component's search function, passing "your query" and "strict" as arguments.
This type of invocation is well-suited for Ajax-enabled applications. ColdFusion 8 introduced the ability to serialize ColdFusion data structures to JSON for consumption on the client.
The ColdFusion server will automatically generate documentation for a component if you navigate to its URL and insert the appropriate code within the component's declarations. This is an application of component introspection, available to developers of ColdFusion components. Access to a component's documentation requires a password. A developer can view the documentation for all components known to the ColdFusion server by navigating to the ColdFusion URL. This interface resembles the Javadoc HTML documentation for Java classes.


=== Custom Tags ===
ColdFusion provides several ways to implement custom markup language tags, i.e. those not included in the core ColdFusion language. These are especially useful for providing a familiar interface for web designers and content authors familiar with HTML but not imperative programming.
The traditional and most common way is using CFML. A standard CFML page can be interpreted as a tag, with the tag name corresponding to the file name prefixed with "cf_". For example, the file IMAP.cfm can be used as the tag "cf_imap". Attributes used within the tag are available in the ATTRIBUTES scope of the tag implementation page. CFML pages are accessible in the same directory as the calling page, via a special directory in the ColdFusion web application, or via a CFIMPORT tag in the calling page. The latter method does not necessarily require the "cf_" prefix for the tag name.
A second way is the developments of CFX tags using Java or C++. CFX tags are prefixed with "cfx_", for example "cfx_imap". Tags are added to the ColdFusion runtime environment using the ColdFusion administrator, where JAR or DLL files are registered as custom tags.
Finally, ColdFusion supports JSP tag libraries from the JSP 2.0 language specification. JSP tags are included in CFML pages using the CFIMPORT tag.


== Interactions with other programming languages ==


=== ColdFusion and Java ===
The standard ColdFusion installation allows the deployment of ColdFusion as a WAR file or EAR file for deployment to standalone application servers, such as Macromedia JRun, and IBM WebSphere. ColdFusion can also be deployed to servlet containers such as Apache Tomcat and Mortbay Jetty, but because these platforms do not officially support ColdFusion, they leave many of its features inaccessible. As of ColdFusion 10 Macromedia JRun was replaced by Apache Tomcat.
Because ColdFusion is a Java EE application, ColdFusion code can be mixed with Java classes to create a variety of applications and use existing Java libraries. ColdFusion has access to all underlying Java classes, supports JSP custom tag libraries, and can access JSP functions after retrieving the JSP page context (GetPageContext()).
Prior to ColdFusion 7.0.1, ColdFusion components could only be used by Java or .NET by declaring them as web services. However, beginning in ColdFusion MX 7.0.1, ColdFusion components can now be used directly within Java classes using the CFCProxy class.
Recently, there has been much interest in Java development using alternate languages such as Jython, Groovy and JRuby. ColdFusion was one of the first scripting platforms to allow this style of Java development.


=== ColdFusion and .NET ===
ColdFusion 8 natively supports .NET within the CFML syntax. ColdFusion developers can simply call any .NET assembly without needing to recompile or alter the assemblies in any way. Data types are automatically translated between ColdFusion and .NET (example: .NET DataTable → ColdFusion Query).
A unique feature for a Java EE vendor, ColdFusion 8 offers the ability to access .NET Assemblies remotely through proxy (without the use of .NET Remoting). This allows ColdFusion users to leverage .NET without having to be installed on a Windows operating system.


== Abbreviations ==

The initialism for the ColdFusion Markup Language is CFML. When ColdFusion templates are saved to disk, they are traditionally given the extension .cfm or .cfml. The .cfc extension is used for ColdFusion Components. The original extension was DBM or DBML, which stood for Database Markup Language. When talking about ColdFusion, most users use the acronym CF and this is used for numerous ColdFusion resources such as user groups (CFUGs) and sites.
CFMX is the common abbreviation for ColdFusion versions 6 and 7 (a.k.a. ColdFusion MX).


== Alternative server environments ==
ColdFusion originated as proprietary technology based on Web technology industry standards. However, it is becoming a less closed technology through the availability of competing products. Such alternative products include :

Lucee - Free, open source CFML engine forked from Railo. Lucee's aim is to provide the functionality of CFML using less resources and giving better performance and to move CFML past its roots and into a modern and dynamic web programming platform. Lucee is backed by community supporters and members of the Lucee Association.
These are discontinued or down :

BlueDragon - Proprietary .NET-based CFML engine and free open source Java-based CFML engine (Open BlueDragon).
Coral Web Builder
IgniteFusion
OpenBD - The open source version of BlueDragon was released as Open BlueDragon (OpenBD) in December 2008.
Railo - Free, open source CFML engine. It comes in three main product editions, and other versions.
SmithProject
The argument can be made that ColdFusion is even less platform-bound than raw Java EE or .NET, simply because ColdFusion will run on top of a .NET app server (New Atlanta), or on top of any servlet container or Java EE application server (JRun, WebSphere, JBoss, Geronimo, Tomcat, Resin Server, Jetty (web server), etc.). In theory, a ColdFusion application could be moved unchanged from a Java EE application server to a .NET application server.


== Vulnerabilities ==
In March 2013, a known issue affecting ColdFusion 8, 9 and 10 left the National Vulnerability Database open to attack. The vulnerability had been identified and a patch released by Adobe for CF9 and CF10 in January.
In April 2013, a ColdFusion vulnerability was blamed by Linode for an intrusion into the Linode Manager control panel website. A security bulletin and hotfix for this had been issued by Adobe a week earlier.
In May 2013, Adobe identified another critical vulnerability, reportedly already being exploited in the wild, which targets all recent versions of ColdFusion on any servers where the web-based administrator and API have not been locked down. The vulnerability allows unauthorized users to upload malicious scripts and potentially gain full control over the server. A security bulletin and hotfix for this was issued by Adobe 6 days later.
In April 2015, Adobe fixed a cross-site scripting (XSS) vulnerability
in Adobe ColdFusion 10 before Update 16, and in ColdFusion 11 before Update 5,
that allowed remote attackers to inject arbitrary web script or HTML; however, it's exploitable only by users who have authenticated through the administration panel.

In September 2019, Adobe fixed two command injection vulnerabilities (CVE-2019-8073) that enabled arbitrary code and an alleyway traversal (CVE-2019-8074).


== See also ==
Adobe ColdFusion Builder
ColdFusion Markup Language
Comparison of programming languages
Fourth-generation programming language


== References ==


== External links ==

Official website
