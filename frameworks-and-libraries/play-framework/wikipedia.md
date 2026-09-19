# Play Framework

Cloned from https://en.wikipedia.org/wiki/Play_Framework.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 27599204.

Play Framework is an open-source web application framework which follows the model–view–controller (MVC) architectural pattern. It is written in Scala and usable from other programming languages that are compiled to JVM bytecode, e.g. Java. It aims to optimize developer productivity by using convention over configuration, hot code reloading and display of errors in the browser.
Support for the Scala programming language has been available since version 1.1 of the framework. In version 2.0, the framework core was rewritten in Scala. Build and deployment was migrated to SBT, and templates use Scala instead of Apache Groovy.


== History ==
Play was created by software developer Guillaume Bort, while working at Zengularity SA (formerly Zenexity). Although the early releases are no longer available online, there is evidence of Play existing as far back as May 2007. In 2007, pre-release versions of the project were available to download from Zenexity's website.


== Motivation ==
Play is heavily inspired by ASP.NET MVC, Ruby on Rails and Django and is similar to this family of frameworks. Play web applications can be written in Scala or Java, in an environment that may be less Java Enterprise Edition-centric. Play uses no Java EE constraints. This can make Play simpler to develop compared to other Java-centric platforms.
Although Play 1.x could also be packaged as WAR files to be distributed to standard Java EE application servers, Play 2.x applications are now designed to be run using the built-in Akka HTTP or Netty web servers exclusively.


== Major differences from Java frameworks ==
Stateless: Play 2 is fully RESTful – there is no Java EE session per connection.
Integrated unit testing: JUnit and Selenium support is included in the core.
API comes with most required elements built-in.
Asynchronous I/O: due to using Akka HTTP as its web server, Play can service long requests asynchronously rather than tying up HTTP threads doing business logic like Java EE frameworks that don't use the asynchronous support offered by Servlet 3.0.
Modular architecture: like Ruby on Rails and Django, Play comes with the concept of modules.
Native Scala support: Play 2 uses Scala internally but also exposes both a Scala API, and a Java API that is deliberately slightly different to fit in with Java conventions, and Play is completely interoperable with Java.


== Testing framework ==
Play provides integration with test frameworks for unit testing and functional testing for both Scala and Java applications. For Scala, integrations with Scalatest and Specs2 are provided out-of-the-box and, for Java, there is integration with JUnit 4. For both languages, there is also integration with Selenium (software). SBT is used to run the tests and also to generate reports. It is also possible to use code coverage tools by using sbt plugins such as scoverage or jacoco4sbt.


== Usage ==
In August 2011, Heroku announced native support for Play applications on its cloud computing platform. This followed module-based support for Play 1.0 on Google App Engine, and documented support on Amazon Web Services.
As of October 2013, the Play Framework was the most popular Scala project on GitHub.
In July 2015, Play was the 3rd most popular Scala library in GitHub, based on 64,562 Libraries. 21.3% of the top Scala projects used Play as their framework of choice.
Corporate users of the Play Framework have included Coursera, HuffPost, Hootsuite, Janrain, LinkedIn, and Connectifier.


== See also ==

Akka (toolkit)
Ebean
Netty (software)
Scala (programming language)


== Literature ==
Wayne Ellis (2010). Introducing the Play Framework.
Alexander Reelsen (2011). Play Framework Cookbook. Packt Publishing. ISBN 1849515522.
Peter Hilton; Erik Bakker & Francisco Canedo (2013). Play for Scala. Manning. ISBN 9781617290794.
Andy Petrella (2013). Learning Play! Framework 2. Packt Publishing. ISBN 978-1-78216-012-0.
Nicolas Leroux; Sietse de Kaper (2014). Play for Java. Manning. ISBN 978-1617290909.
Julien Richard-Foy (2014). Play Framework Essentials. Packt Publishing. ISBN 978-1783982400.
Shiti Saxena (2015). Mastering Play Framework for Scala. Packt Publishing. ISBN 978-1783983803.
Alexander Reelsen; Giancarlo Inductivo (2015). Play Framework Cookbook (2nd ed.). Packt Publishing. ISBN 978-1783982400.
PremKumar Karunakaran (2020). Introducing Play Framework (2nd ed.). Apress. ISBN 978-1-4842-5644-2.


== References ==


== External links ==
Play Framework home page
