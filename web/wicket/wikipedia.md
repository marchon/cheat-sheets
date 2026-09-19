# Apache Wicket

Cloned from https://en.wikipedia.org/wiki/Apache_Wicket.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 1934392.

Apache Wicket, commonly referred to as Wicket, is a component-based web application framework for the Java programming language conceptually similar to JavaServer Faces and Tapestry.  It was originally written by Jonathan Locke in April 2004.  Version 1.0 was released in June 2005. It graduated into an Apache top-level project in June 2007.


== Rationale ==
Traditional model-view-controller (MVC) frameworks work in terms of whole requests and whole pages.  In each request cycle, the incoming request is mapped to a method on a controller object, which then generates the outgoing response in its entirety, usually by pulling data out of a model to populate a view written in specialized template markup.  This keeps the application's flow-of-control simple and clear, but can make code reuse in the controller difficult.
In contrast, Wicket is closely patterned after stateful GUI frameworks such as Swing.  Wicket applications are trees of components, which use listener delegates to react to HTTP requests against links and forms in the same way that Swing components react to mouse and keystroke events. Wicket is categorized as a component-based framework.


== Design ==
Wicket uses plain XHTML for templating (which enforces a clear separation of presentation and business logic and allows templates to be edited with conventional WYSIWYG design tools).  Each component is bound to a named element in the XHTML and becomes responsible for rendering that element in the final output. The page is simply the top-level containing component and is paired with exactly one XHTML template.  Using a special tag, a group of individual components may be abstracted into a single component called a panel, which can then be reused whole in that page, other pages, or even other panels.
Each component is backed by its own model, which represents the state of the component. The framework does not have knowledge of how components interact with their models, which are treated as opaque objects automatically serialized and persisted between requests. More complex models, however, may be made detachable and provide hooks to arrange their own storage and restoration at the beginning and end of each request cycle.  Wicket does not mandate any particular object-persistence or ORM layer, so applications often use some combination of Hibernate objects, EJBs or POJOs as models.
In Wicket, all server side state is automatically managed. You should never directly use an HttpSession object or similar wrapper to store state. Instead, state is associated with components. Each server-side page component holds a nested hierarchy of stateful components, where each component's model is, in the end, a POJO (Plain Old Java Object).
Wicket aims for simplicity. There are no configuration files to learn in Wicket. Wicket is a simple class library with a consistent approach to component structure.


== Example ==
A Hello World Wicket application, with four files:

HelloWorld.html
The XHTML template.
 
HelloWorld.java
The page component that will be bound to the template.  It, in turn, binds a child component (the Label component named "message").

HelloWorldApplication.java
The main application class, which routes requests for the homepage to the HelloWorld page component.

web.xml
The servlet application Deployment Descriptor, which installs Wicket as the default handler for the servlet and arranges for HelloWorldApplication to be instantiated at startup.


== Components ==
Basic components like form, links, repeaters, and so on are built-in.


== Releases ==


== See also ==

Vaadin
Tapestry
Click
ZK
Richfaces
Echo


== References ==


=== Notes ===


== External links ==
Official website
