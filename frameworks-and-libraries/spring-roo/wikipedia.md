# Spring Roo

Cloned from https://en.wikipedia.org/wiki/Spring_Roo.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 24719742.

Spring Roo is an open-source software tool that uses convention-over-configuration principles to provide rapid application development of Java-based enterprise software. 
The project has been deprecated and active development has ended.


== Motivation and history ==
Spring Roo's mission statement is to "fundamentally improve Java developer productivity without compromising engineering integrity or flexibility".
The technology was first demonstrated during the opening keynote at the SpringOne Europe developer conference on 27 April 2009, with an initial alpha release concurrently being published. During the keynote an application was built live on-stage that would be used by conference attendees to vote on the preferred name for the project (which at that time was codenamed "Roo" within SpringSource). Ultimately the name "Spring Roo" was preferred over alternatives including Spring Boost, Spring Spark, Spring HyperDrive and Spring Dart.
Several releases followed, with the Roo 1.0.0.RELEASE (general availability) released in December 2009. In October 2010, Spring Roo 1.1.0.RELEASE was released. The 1.1.0 release moved to an OSGi foundation with associated add-on discovery model, plus added support for incremental database reverse engineering, Spring MVC page complexity reduction, Google Web Toolkit, Google App Engine, Apache Solr, JSON and smaller features like serializable automation. 
In 2014 DISID took over the leadership of the open source framework Spring Roo after a partnership agreement with Pivotal.
DSID and VMware deprecated Spring Roo and announced the end of active development in 2019 and the repository was archived in 2022.


== Standards and technology compatibility ==
Roo's default installation facilitates the creation of applications that comply with the following standards and major technologies:

Apache ActiveMQ (as an embedded JMS implementation)
Apache Maven (version 3.2 or above)
Apache Tomcat (embedded execution support)
AspectJ (used for AOP plus mixins to achieve separation of concerns)
AspectJ Development Tools (Eclipse plugin)
Bootstrap (version 3.3.6 or above)
Cloud computing (via SpringSource Cloud Foundry, Google App Engine and VMforce)
Eclipse IDE (concurrent execution and project metadata creation)
EclipseLink (as a JPA implementation)
Hibernate (as a JPA implementation)
Java Bean Validation (JSR 303) (including Hibernate Validator)
Java API for XML Web Services (both services and clients)
Java Message Service (both message producers and consumers)
Java Persistence API (multiple implementations)
Java Transaction API (via Spring transaction abstraction)
Java (version 5, 6 or 7). Java 7 is supported since Roo 1.2.4.
JQuery (version 1.11 or above)
JSON (REST support)
JUnit (automated tests for user projects)
Log4j (installation and configuration)
OSGi (the Roo tool is built on OSGi)
Representational State Transfer (REST)
Spring Boot (version 1.4 or above)
Spring Data JPA (version 1.10 or above)
Spring Framework (version 4 or above)
Spring Security (version 4 or above)
Spring Web Flow (installation and flow definition)
SpringSource Tool Suite (STS has an embedded Roo shell and Roo command helpers)
Thymeleaf (version 3 or above)
The above list can be augmented through additional Roo add-ons, which provide Roo's method of extensibility.


== User interface ==
Spring Roo's main user interface is a command-line shell. The shell provides both a command-line interface and also a mechanism to host plug-ins (which are called "add-ons" in Roo). One key design goal of Roo is to ensure a user can continue to work in a "natural way", which typically means using their preferred integrated development environment (IDE) or text editor for most tasks. As such Roo is often loaded in a separate window to the IDE or text editor, and will monitor the file system for changes made by the user outside of Roo. A startup-time scan of a user's project is also performed to determine any changes that may have been made while Roo was not running.
The user interface shell supports extensive usability features including command-line completion (i.e. press TAB), online help, hinting (a form of context-sensitive help) and contextual awareness (which provides automatic inference of likely intentions based on recent activity). This allows a user to create a new software project via the Roo shell, or use Roo on an existing project. The following is an example of the commands used by Roo to create a new application plus the Spring Boot Maven plugin run goal to compile and run the application using an embedded HTTP server:

The above commands did not need to be typed in full, but rather were completed using TAB. Additionally, the "hint" command could have been used to acquire help at any time.


== Architecture ==
Roo operates by generating AspectJ inter-type declarations (otherwise known as mixins or introductions). This achieves separation of concerns, as the code maintained by Roo is in a different compilation unit from the code a user writes. This means Roo can incrementally modify the AspectJ inter-type declarations that it needs to and leave all other files intact.
Spring Roo uses add-ons to provide all the functionality within and on top of an OSGi runtime system based on Apache Felix.


== Differentiation ==
Spring Roo differs from other convention-over-configuration rapid application development tools like so:

Java platform productivity: Roo provides a productivity solution for Java developers. It does not require the user to program in any language other than Java. It also uses mainstream Java enterprise application standards and technologies (as listed above) to maximize reuse of existing developer knowledge, skills and experience.
Usability: Roo's shell is designed to provide a discoverable, easy-to-use environment that minimizes training requirements. Roo annotations all start with @Roo to facilitate code assist (command line completion in IDEs). Users can use their IDE for all operations and do not need to be aware of Roo running. Roo also supports users editing their files when Roo is not running.
No runtime: Roo does not provide a runtime API or require specific runtime components. This ensures there is no Roo-related CPU, memory and disk storage resource consumption at runtime. Roo code is optimized for small-footprint cloud deployment and high scalability use cases.
Avoids lock-in: Roo can be rapidly removed from a user project, which is useful to protect against vendor lock-in. This is possible because there is no runtime component to remove, @Roo annotations are "source retention" only (ensuring they are not preserved in compiled *.class files) and Roo's AspectJ inter-type declarations can be "pushed in" to standard *.java compilation units.
Extensibility: Roo's separation of core infrastructure and base add-ons intends to allow third parties to easily extend Roo.


== See also ==

Grails (framework)
Griffon (framework) – A Desktop framework inspired by Grails
Play Framework


== References ==


== External links ==
Official website
