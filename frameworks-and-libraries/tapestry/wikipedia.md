# Apache Tapestry

Cloned from https://en.wikipedia.org/wiki/Apache_Tapestry.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 2052309.

Apache Tapestry is an open-source component-oriented Java web application framework conceptually similar to JavaServer Faces and Apache Wicket. Tapestry was created by Howard Lewis Ship, and was adopted by the Apache Software Foundation as a top-level project in 2006.
Tapestry emphasizes simplicity, ease of use, and developer productivity. It adheres to the Convention over Configuration paradigm, eliminating almost all XML configuration. Tapestry uses a modular approach to web development by having a strong binding between each user interface component (object) on the web page and its corresponding Java class. This component-based architecture borrows many ideas from WebObjects.


== Notable features ==
Live Class Reloading
Tapestry monitors the file system for changes to Java page classes, component classes, service implementation classes, HTML templates and component property files, and it hot-swaps the changes into the running application without requiring a restart. This provides a very short code-save-view feedback cycle that is claimed to greatly improve developer productivity.
Component-based
Pages may be constructed with small nestable components, each having a template and a component class. Custom components are purportedly trivial to construct.
Convention over configuration
Tapestry uses naming conventions and annotations, rather than XML, to configure the application.
Spare use of HTTPSession
By making minimal use of the HTTPSession, Tapestry is designed to be highly efficient in a clustered, session-replicated environment.
Post/Redirect/Get
Most form submissions follow the Post/Redirect/Get (PRG) pattern, which reduces multiple form submission accidents and makes URLs friendlier and more bookmarkable, along with enabling the browser Back and Refresh buttons to operate normally.
Inversion of Control (IoC)
Tapestry is built on a lightweight Inversion of Control layer with similarities to Google Guice, but designed to make nearly all aspects of Tapestry's behavior configurable and replaceable.


== Hello World Example ==
A minimal, templated Tapestry application needs only three files:

HelloWorld.tml
The (X)HTML template for the /helloworld page. Tapestry templates can contain any well-formed (X)HTML markup.
 
HelloWorld.java
The page class associated with the template. Here, it merely provides a *username* property that the template can access.

web.xml
The servlet application Deployment Descriptor, which installs Tapestry as a servlet filter.


== Class transformation ==
Tapestry uses bytecode manipulation to transform page and component classes at runtime. This approach allows the page and component classes to be written as simple POJOs, with a few naming conventions and annotations potentially triggering substantial additional behavior at class load time. Tapestry versions 5.0, 5.1 and 5.2 used the Javassist bytecode manipulation library. Subsequent versions replaced Javassist with a new bytecode manipulation layer called Plastic that is based on ObjectWeb ASM.


== Client-side support ==
Tapestry 5 versions up through 5.3 bundled the Prototype and script.aculo.us JavaScript frameworks, along with a Tapestry-specific library, so as to support Ajax operations as first-class citizens. Third party modules are available to integrate jQuery instead of, or in addition to, Prototype/Scriptaculous.
Starting with version 5.4, Tapestry includes a new JavaScript layer that removes built-in components' reliance on Prototype, allowing jQuery or another JavaScript framework to be plugged in.
Version 5.4 also introduces support for JavaScript modules using the RequireJS module loading system.


== Core principles ==
The Tapestry project documentation cites four "principles" that govern all development decisions for Tapestry, starting with version 5 in 2008:

Static Structure, Dynamic Behavior—page and component structure is essentially static, eliminating the need to construct (and store in session memory) large page and component trees.
Adaptive API—the framework is designed to adapt to the code, rather than having the code adapt to the framework
Differentiate Public vs. Internal APIs—all APIs are explicitly "internal" (private) except those that are necessarily public.
Ensure Backwards Compatibility—The Tapestry developers are reportedly committed to ensuring that upgrading to the latest version of Tapestry is always easy.


== Criticism ==
Tapestry has been criticized as not being backward-compatible across major versions, especially noted in the transition from version 4 to version 5, where no clean migration path was available for existing applications. Project team members have acknowledged this as a major problem for Tapestry's users in the past, and backward compatibility was made a major design goal for Tapestry going forward. From early on in the development of version 5, backward compatibility was listed as one of Tapestry's four new "Core Principles", and two of the other three were intended to make the evolution of the framework possible without sacrificing backward compatibility. Project team members claim that all Tapestry releases since 5.0 have been highly backward compatible.
Early criticisms of Tapestry 5 also mentioned documentation as a shortcoming. Project members now claim that this deficiency has been largely addressed with a thoroughly revised and updated User's Guide and other documentation.
Since version 5.0, Tapestry has bundled the Prototype and Scriptaculous JavaScript libraries. According to Howard Lewis Ship, in the 2008-2009 timeframe these were reasonable choices. Since then, however, Prototype's popularity has declined, and jQuery's has risen dramatically. In response, the Tapestry community developed modules that allowed jQuery to be used in addition to, or instead of, Prototype. Meanwhile, the current version of Tapestry, 5.4, removes the dependency on Prototype entirely, replacing it with a compatibility layer into which either jQuery or Prototype (or potentially any other JavaScript framework) can be plugged.


== Relation to other frameworks ==
According to Howard Lewis Ship, Tapestry was initially conceived as an attempt to implement in Java some of the general concepts and approaches found in WebObjects, which was at that time written in Objective-C and closed-source.
Apache Wicket was developed as a response to the complexity of early versions of Tapestry, according to Wicket originator Jonathan Locke.
Facelets, the default view technology in JavaServer Faces, was reportedly inspired by early versions of Tapestry, as an attempt to fill the need for "a framework like Tapestry, backed by JavaServer Faces as the industry standard".


== History ==


== See also ==
Apache Wicket
Comparison of web frameworks
Facelets
Java EE
Java view technologies and frameworks


== References ==


=== Notes ===


== External links ==
Official website
