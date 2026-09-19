# Business Process Execution Language

Cloned from https://en.wikipedia.org/wiki/Business_Process_Execution_Language.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 334947.

The Web Services Business Process Execution Language (WS-BPEL), commonly known as BPEL (Business Process Execution Language), is an OASIS standard executable language for specifying actions within business processes with web services. Processes in BPEL export and import information by using web service interfaces exclusively.


== Overview ==
One can describe web service interactions in two ways: as executable business processes and as abstract business processes.

An executable business process: models an actual behavior of a participant in a business interaction.
An abstract business process: is a partially specified process that is not intended to be executed. Contrary to Executable Processes, an Abstract Process may hide some of the required concrete operational details. Abstract Processes serve a descriptive role, with more than one possible use case, including observable behavior and/or process template.
WS-BPEL aims to model the behavior of processes, via a language for the specification of both Executable and Abstract Business Processes. By doing so, it extends the Web Services interaction model and enables it to support business transactions. It also defines an interoperable integration model that should facilitate the expansion of automated process integration both within and between businesses. Its development came out of the notion that programming in the large and programming in the small required different types of languages.
As such, it is serialized in XML and aims to enable programming in the large.


== Programming in the large/small ==
The concepts of programming in the large and programming in the small distinguish between two aspects of writing the type of long-running asynchronous processes that one typically sees in business processes:

Programming in the large generally refers to the high-level state transition interactions of a process. BPEL refers to this concept as an Abstract Process. A BPEL Abstract Process represents a set of publicly observable behaviors in a standardized fashion. An Abstract Process includes information such as when to wait for messages, when to send messages, when to compensate for failed transactions, etc.
Programming in the small, in contrast, deals with short-lived programmatic behavior, often executed as a single transaction and involving access to local logic and resources such as files, databases, et cetera.


== History ==
The origins of WS-BPEL go back to Web Services Flow Language (WSFL) and Xlang.
In 2001, IBM and Microsoft had each defined their own fairly similar, "programming in the large" languages: WSFL (Web Services Flow Language) and Xlang, respectively. Microsoft even went ahead and created a scripting variant called XLANG/s which would later serve as the basis for their Orchestrations services inside their BizTalk Server. They specifically documented that this language "is proprietary and is not fully documented."
With the advent and popularity of BPML, and the growing success of BPMI.org and the open BPMS movement led by JBoss and Intalio Inc., IBM and Microsoft decided to combine these languages into a new language, BPEL4WS. In April 2003, BEA Systems, IBM, Microsoft, SAP, and Siebel Systems submitted BPEL4WS 1.1 to OASIS for standardization via the Web Services BPEL Technical Committee. Although BPEL4WS appeared as both a 1.0 and 1.1 version, the OASIS WS-BPEL technical committee voted on 14 September 2004 to name their spec "WS-BPEL 2.0". (This change in name aligned BPEL with other web service standard naming conventions which start with "WS-" (similar to WS-Security) and took account of the significant enhancements made between BPEL4WS 1.1 and WS-BPEL 2.0.) If not discussing a specific version, the moniker BPEL is commonly used.
In June 2007, Active Endpoints, Adobe Systems, BEA, IBM, Oracle, and SAP published the BPEL4People and WS-HumanTask specifications, which describe how human interaction in BPEL processes can be implemented.


== Topics ==


=== Design goals ===
There were ten original design goals associated with BPEL:

Define business processes that interact with external entities through web service operations defined using Web Services Description Language (WSDL) 1.1, and that manifest themselves as Web services defined using WSDL 1.1. The interactions are "abstract" in the sense that the dependence is on portType definitions, not on port definitions.
Define business processes using an XML-based language. Do not define a graphical representation of processes or provide any particular design methodology for processes.
Define a set of Web service orchestration concepts that are meant to be used by both the external (abstract) and internal (executable) views of a business process. Such a business process defines the behavior of a single autonomous entity, typically operating in interaction with other similar peer entities. It is recognized that each usage pattern (i.e., abstract view and executable view) will require a few specialized extensions, but these extensions are to be kept to a minimum and tested against requirements such as import/export and conformance checking that link the two usage patterns.
Provide both hierarchical and graph-like control regimes, and allow their use to be blended as seamlessly as possible. This should reduce the fragmentation of the process modeling space.
Provide data manipulation functions for the simple manipulation of data needed to define process data and control flow.
Support an identification mechanism for process instances that allows the definition of instance identifiers at the application message level. Instance identifiers should be defined by partners and may change.
Support the implicit creation and termination of process instances as the basic lifecycle mechanism. Advanced lifecycle operations such as "suspend" and "resume" may be added in future releases for enhanced lifecycle management.
Define a long-running transaction model that is based on proven techniques like compensation actions and scoping to support failure recovery for parts of long-running business processes.
Use Web Services as the model for process decomposition and assembly.
Build on Web services standards (approved and proposed) as much as possible in a composable and modular manner.


=== The BPEL language ===
BPEL is an orchestration language, and not a choreography language. The primary difference between orchestration and choreography is executability and control. An orchestration specifies an executable process that involves message exchanges with other systems, such that the message exchange sequences are controlled by the orchestration designer. A choreography specifies a protocol for peer-to-peer interactions, defining, e.g., the legal sequences of messages exchanged with the purpose of guaranteeing interoperability. Such a protocol is not directly executable, as it allows many different realizations (processes that comply with it). A choreography can be realized by writing an orchestration (e.g., in the form of a BPEL process) for each peer involved in it. The orchestration and the choreography distinctions are based on analogies: orchestration refers to the central control (by the conductor) of the behavior of a distributed system (the orchestra consisting of many players), while choreography refers to a distributed system (the dancing team) which operates according to rules (the choreography) but without centralized control.
BPEL's focus on modern business processes, plus the histories of WSFL and XLANG, led BPEL to adopt web services as its external communication mechanism. Thus BPEL's messaging facilities depend on the use of the Web Services Description Language (WSDL) 1.1 to describe outgoing and incoming messages.
In addition to providing facilities to enable sending and receiving messages, the BPEL programming language also supports:

A property-based message correlation mechanism
XML and WSDL typed variables
An extensible language plug-in model to allow writing expressions and queries in multiple languages: BPEL supports XPath 1.0 by default
Structured-programming constructs including if-then-elseif-else, while, sequence (to enable executing commands in order) and flow (to enable executing commands in parallel)
A scoping system to allow the encapsulation of logic with local variables, fault-handlers, compensation-handlers and event-handlers
Serialized scopes to control concurrent access to variables.


=== Relationship of BPEL to BPMN ===
There is no standard graphical notation for WS-BPEL, as the OASIS technical committee decided this was out of scope. Some vendors have invented their own notations. These notations take advantage of the fact that most constructs in BPEL are block-structured (e.g., sequence, while, pick, scope, etcetera.) This feature enables a direct visual representation of BPEL process descriptions in the form of structograms, in a style reminiscent of a Nassi–Shneiderman diagram.
Others have proposed to use a substantially different business process modeling language, namely Business Process Model and Notation (BPMN), as a graphical front-end to capture BPEL process descriptions. As an illustration of the feasibility of this approach, the BPMN specification includes an informal and partial mapping from BPMN to BPEL 1.1. A more detailed mapping of BPMN to BPEL has been implemented in a number of tools, including an open-source tool known as BPMN2BPEL. However, the development of these tools has exposed fundamental differences between BPMN and BPEL, which make it very difficult, and in some cases impossible, to generate human-readable BPEL code from BPMN models. Even more difficult is the problem of BPMN-to-BPEL round-trip engineering: generating BPEL code from BPMN diagrams and maintaining the original BPMN model and the generated BPEL code synchronized, in the sense that any modification to one is propagated to the other.


=== Adding 'programming in the small' support to BPEL ===
BPEL's control structures such as 'if-then-elseif-else' and 'while' as well as its variable manipulation facilities depend on the use of 'programming in the small' languages to provide logic. All BPEL implementations must support XPath 1.0 as a default language. But the design of BPEL envisages extensibility so that systems builders can use other languages as well. BPELJ is an effort related to JSR 207 that may enable Java to function as a 'programming in the small' language within BPEL.


=== BPEL4People ===
Despite wide acceptance of Web services in distributed business applications, the absence of human interactions was a significant gap for many real-world business processes.
To fill this gap, BPEL4People extended BPEL from orchestration of Web services alone to orchestration of role-based human activities as well.


==== Objectives ====
Within the context of a business process BPEL4People

supports role-based interaction of people
provides means of assigning users to generic human roles
takes care to delegate ownership of a task to a person only
supports scenario as
four-eyes scenario
nomination
escalation
chained execution
by extending BPEL with additional independent syntax and semantic.
The WS-HumanTask specification introduces the definition of human tasks and notifications, including their properties, behavior and a set of operations used to manipulate human tasks. A coordination protocol is introduced in order to control autonomy and life cycle of service-enabled human tasks in an interoperable manner.
The BPEL4People specification introduces a WS-BPEL extension to address human interactions in WS-BPEL as a first-class citizen. It defines a new type of basic activity which uses human tasks as an implementation, and allows specifying tasks local to a process or use tasks defined outside of the process definition. This extension is based on the WS-HumanTask specification.


=== WS-BPEL 2.0 ===
Version 2.0 introduced some changes and new features:

New activity types: repeatUntil, validate, forEach (parallel and sequential), rethrow, extensionActivity, compensateScope
Renamed activities: switch/case renamed to if/else, terminate renamed to exit
Termination Handler added to scope activities to provide explicit behavior for termination
Variable initialization
XSLT for variable transformations (New XPath extension function bpws:doXslTransform)
XPath access to variable data (XPath variable syntax $variable[.part]/location)
XML schema variables in Web service activities (for WS-I doc/lit style service interactions)
Locally declared messageExchange (internal correlation of receive and reply activities)
Clarification of Abstract Processes (syntax and semantics)
Enable expression language overrides at each activity


== See also ==
BPEL4People
BPELscript
Business Process Model and Notation
Business Process Modeling
List of BPEL engines
Web Services Conversation Language
Workflow
WS-CDL
XML Process Definition Language
Yet Another Workflow Language


== References ==


== Further reading ==
Books on BPEL 2.0
SOA for the Business Developer: Concepts, BPEL, and SCA. ISBN 978-1-58347-065-7
