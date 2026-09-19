# Vaadin

Cloned from https://en.wikipedia.org/wiki/Vaadin.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 22899208.

Vaadin (Finnish pronunciation: [ˈʋɑːdin]) is an open-source web application development platform for Java. Vaadin includes a set of Web Components, a Java web framework, and a set of tools that enable developers to implement modern web graphical user interfaces (GUI) using the Java programming language only (instead of HTML and JavaScript), TypeScript only, or a combination of both.


== History ==
Development began as the Millstone web framework in 2000. It was first released as open-source  in 2002. Millstone introduced a component-oriented programming model for the web and an Ajax-based client communication and rendering engine. As a result, a large part of Vaadin's server-side API remains compatible with Millstone's Swing-like APIs.
In early 2007 the product name was changed to IT Mill Toolkit and version 4 was released. It used a proprietary JavaScript Ajax-implementation for the client-side rendering, which made it rather complicated to implement new widgets. By the end of the year 2007 the proprietary client-side implementation was abandoned and GWT was integrated on top of the server-side components. At the same time, the product license was changed to the open source Apache License 2.0. The first production-ready release of IT Mill Toolkit 5 was made on March 4, 2009, after an over one year beta period.
On September 11, 2008, it was publicly announced that Michael Widenius–the main author of the original version of MySQL–invested in IT Mill, the Finnish developer of Vaadin. The size of the investment is undisclosed.
On May 20, 2009, IT Mill Toolkit changed its name to Vaadin Framework. The name originates from the Finnish word for doe, more precisely put, a female reindeer. It can also be translated from Finnish as "I insist". In addition to the name change, a pre-release of version 6 along with a community website was launched. Later, IT Mill Ltd, the company behind the open source Vaadin Framework, changed its name to Vaadin Ltd.
On March 30, 2010, Vaadin Directory was opened. It added a channel for distributing add-on components to the core Vaadin Framework, both for free or commercially. On launch date, there were 95 add-ons already available for download.


== Vaadin Flow (Java API) ==
Vaadin Flow (formerly Vaadin Framework) is a Java web framework for building web applications and websites. Vaadin Flow's programming model allows developers to use Java as the programming language for implementing User Interfaces (UIs) without having to directly use HTML or JavaScript. Vaadin Flow features a server-side architecture which means that most of the UI logic runs securely on the server reducing the exposure to attackers. On the client-side, Vaadin Flow is built on top of Web Component standards. The client/server communication is automatically handled through WebSocket or HTTP with light JSON messages that update both, the UI in the browser and the UI state in the server.

Vaadin Flow's Java API includes classes such as TextField, Button, ComboBox, Grid, and many others that can be configured, styled, and added into layout objects instances of classes such as VerticalLayout, HorizontalLayout, SplitLayout, and others. Behaviour is implemented by adding listeners to events such as clicks, input value changes, and others. Views are created by custom Java classes that implement another UI component (custom or provided by the framework). This view classes are annotated with @Route to expose them to the browser with a specific URL. The following example illustrates these concepts: The following is a screenshot of the previous example: 


== Hilla (TypeScript API) ==
Hilla (formerly Vaadin Fusion) is a web framework that integrates Spring Boot Java backends with reactive front ends implemented in TypeScript. This combination offers a fully type-safe development platform by combining server-side business logic in Java and type-safety in the client side with the TypeScript programming language. Views are implemented using Lit—a lightweight library for creating Web Components. The following is an example of a basic view implemented with Hilla:
Starting in October 2025, Hilla is being discontinued as a stand-alone product and merged into Flow.


== Vaadin's UI components ==
Vaadin includes a set of User Interface (UI) components implemented as Web Components. These components include a server-side Java API (Vaadin Flow) but can also be used directly in HTML documents as well. Vaadin's UI components work with mouse and touch events, can be customized with CSS, are compatible with WAI-ARIA, include keyboard and screen readers support, and support right-to-left languages.
The following table shows a list of the UI components included in Vaadin:


== Vaadin Copilot ==
Vaadin Copilot is a browser-based development tool that runs inside a Vaadin application during development. It provides visual drag-and-drop editing of UI layouts, AI-assisted code generation, Figma-to-code import, accessibility checking, and UI test generation directly within the running application.
Copilot operates through a toolbar with four working modes: Play (normal application interaction), Inspect (read-only structure exploration), Test (accessibility and UI test generation), and Edit (drag-and-drop layout changes and AI-powered code modifications).
Starting with Vaadin 25.1, all Copilot features—including source code manipulation and AI assistance—are available at no cost to any developer with a Vaadin.com account. IDE integrations are available for IntelliJ IDEA, Visual Studio Code, and Eclipse.


== Certifications ==
Vaadin offers certification tracks to prove that a developer is proficient with Vaadin Flow:

Certified Vaadin 25 Developer
To pass the certification, a developer should go through the documentation, follow the training videos, and take an online test.
Previous (now unavailable) certifications included:

Vaadin Online Exam for Vaadin 7 Certified Developer
Vaadin Online Exam for Vaadin 8 Certified Developer
Certified Vaadin 14 Developer
Certified Vaadin 14 Professional


== Vaadin Enterprise Edition ==
Vaadin Enterprise Edition is a commercially licensed distribution of Vaadin that provides additional guarantees and tools aimed at organisations deploying long-lived, regulated, or security-sensitive applications.
The primary technical differentiator is extended long-term support (LTS): Enterprise subscribers receive security fixes and maintenance patches for 15 years from the release of the next major version, covering periods that routinely extend to 15–18 years from the initial release. CVE notifications are provided to subscribers before public disclosure, and security fixes are delivered ahead of the open-source release. Annual third-party audits produce an Accessibility Conformance Report (ACR/VPAT) covering WCAG 2.1 AA, Section 508, and EN 301 549.


== See also ==
List of rich web application frameworks


== References ==


== Further reading ==
Duarte, A. (2021) Practical Vaadin: Developing Web Applications in Java. Apress.
Duarte, A. (2018) Data-Centric Applications with Vaadin 8 Archived 2018-04-30 at the Wayback Machine. Packt Publishing.
Frankel, N. (2013) Learning Vaadin 7, Second Edition. Packt Publishing.Duarte, A. (2013) Vaadin 7 UI Design by Example: Beginner's Guide. Packt Publishing.Holan, J., & Kvasnovsky, O. (2013) Vaadin 7 Cookbook. Packt Publishing.Taylor C. (2012) Vaadin Recipes. Packt Publishing.Frankel, N. (2011) Learning Vaadin. Packt Publishing.Grönroos, M. (2010) Book of Vaadin. Vaadin Ltd.


== External links ==
Official website 
Vaadin on GitHub
