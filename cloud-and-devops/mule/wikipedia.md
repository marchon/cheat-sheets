# Mule (software)

Cloned from https://en.wikipedia.org/wiki/Mule_(software).

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 4148670.

Mule is a lightweight enterprise service bus (ESB) and integration framework provided by MuleSoft. It has a Java-based platform and can also act as broker for interactions between other platforms such as .NET using web services or sockets.
It has a scalable and distributable object broker architecture that can manage interactions across legacy systems, in-house applications, and modern transports and protocols.


== Supporting tools ==


=== Design and development tools ===
Anypoint Studio: An Eclipse-based graphical development environment for designing, testing, and running Mule flows. It consists of two types of editors for development: a visual editor and an XML editor.
Anypoint Enterprise Security: A suite of security-related features for secure access and transactions to Mule applications.
Mule Healthcare Toolkit: Provided to process HL7 standard messages used in healthcare organizations.
Mule IDE (now deprecated): A set of Eclipse plug-ins for developing, deploying, and managing Mule projects.


=== Management tools ===
Mule Management Console: A user interface that provides a run-time management facility for deployment to the Mule Repository and clusters.
Mule has an integration engine, but the community edition lacks support for Advanced Management interfaces. MuleSoft offers an Enterprise Edition of Mule that provides a management console, a Service registry, and higher availability.


==== Cloudhub ====
Cloudhub is Mulesoft's Cloud-based integration platform as a service (iPaaS) designed to connect apps, data, and devices with integration connectors (like one to Twitter, etc.).


== Mule ESB and messaging ==


=== AMQP support ===
AMQP (Advanced Message Queuing Protocol) support is based on the RabbitMQ Java Client and supports AMQP up to 0.9.1.


=== JMS support ===
Jakarta Messaging is a Message-oriented middleware API provided by Oracle for communication between different components of an application. This provides reliable, loosely coupled, and asynchronous message-based communication, supporting two models: point-to-point (queues) and publish-subscribe (topics). Mule supports all functionality of JMS specification versions 1.0.2b and 1.1, and provides an endpoint for the same.


=== WMQ support ===
WMQ or Websphere MQ is an IBM Message Oriented Middleware product for communication for distributed systems. Mule also provides support for WMQ called Mule WMQ Transport which works with 7.0, 7.1, and 7.5 versions and provides an endpoint for the same.


== Universal Message Object ==
The Universal Message Object Application Programming Interface is part of high-level design methodologies used to describe and define aspects of a data object used in conjunction with the Mule ESB. The idea is to, by staged events, wrap the work into sensible bundles and process it in stages that can conform to models of transaction-based processing that are useful in time or mission-critical applications such as financial transactions, where subsequent successful outcomes are required to permit the desired outcome. But if the user fails to supply needed data or a run-time error occurs, then the model will allow for state-full back-off, meaning "no harm done", the user may then complete a transaction without losing too much work or cancelling an entire transaction.
Universal Message Object defines the parameters that the program will use for internal messaging communications and its components to set and get variables based upon the user's needs and the program's functionality.


== References ==


== Further reading ==
Tijs Rademakers and Jos Dirksen, "Open-Source ESBs in Action" (Manning Publications: Oct 2008, ISBN 1-933988-21-5; ISBN 978-1-933988-21-4)
Peter Delia and Antoine Borg, "Mule 2: A Developer’s Guide" (Apress: Nov 2008, ISBN 1-4302-0981-X; ISBN 978-1-4302-0981-2),
David Dossot and John D'Emic, "Mule in Action" (Manning Publications: Apr 2009, ISBN 1-933988-96-7; ISBN 978-1-933988-96-2)
Getting Started with Mule Cloud Connect (O'Reilly Media: Dec 2012, Print ISBN 978-1-4493-3100-9; ISBN 1-4493-3100-9; Ebook ISBN 978-1-4493-3095-8; ISBN 1-4493-3095-9)
David Dossot, John D'Emic and Victor Romero, "Mule in Action, Second Edition" (Manning Publications, Early Access Program)
Hanson, Jeff (January 31, 2005), "Event-driven services in SOA", JavaWorld, retrieved 2020-07-21


== External links ==
Official website
