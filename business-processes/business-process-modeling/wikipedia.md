# Business process modeling

Cloned from https://en.wikipedia.org/wiki/Business_process_modeling.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 1155559.

Business process modeling (BPM) is the action of modeling processes of an enterprise. BPM is used to analyze, improve, and possibly automate business processes. BPM is typically performed by business analysts in collaboration with subject matter experts. It is primarily used in business process management, software development, and systems engineering. BPM can also be automatically generated through IT systems, such as event logs and other data.
BPM has many applications in business process management. There are multiple methods of modeling and notations that are recommended, BPMN being the most common.


== Overview ==
According to the Association of Business Process Management Professionals (ABPMP), BPM is one of the five key disciplines within business process management, alongside process analysis, design, performance measurement, and transformation.
BPM typically depends on process analysis to document current operations and on process design to define desired processes.
The focus of BPM is on representing the flow of actions or activities. Hermann J. Schmelzer and Wolfgang Sesselmann define it as "the cross-functional identification of value-adding activities that generate specific services expected by the customer and whose results have strategic significance for the company". These activities can extend beyond company boundaries and may include interactions with customers, suppliers, or even competitors. In addition to activities, other elements such as data and business objects, organizational roles and responsibilities, resources, guidelines, and performance indicators can also be modeled.
Incorporating more of these elements increases the accuracy of the model but also its complexity. To maintain clarity and transparency, Schmelzer and Sesselmann recommend using "views", which allow models to focus on specific perspectives while reducing overall complexity. Views are also referred to as design dimensions or perspectives. While creating models for each process separately with views, however, redundancies are introduced which may increase maintenance effort and jeopardize the consistency of the models.
BPM is also a central aspect of holistic company mapping – which deals with the mapping of the corporate mission statement, corporate governance, organizational structure, process organization, application architecture, regulations, and market strategy. According to the European Association of Business Process Management (EABPM), the top level for structuring business process models are base on three different types of end-to-end business processes, namely Leadership, Execution, and Support processes.
Execution processes are then organized at the next level in supply chain management (SCM), customer relationship management (CRM), and product lifecycle management (PLM). Standard models of large organizations and industry associations such as the SCOR model can also be integrated into business process modeling.


== History ==
Techniques to model business processes, such as the flow chart, functional flow block diagram, control flow diagram, Gantt chart, PERT diagram, and IDEF have emerged since the beginning of the 20th century. The Gantt charts were among the first to arrive around 1899, the flow charts in the 1920s, functional flow block diagram and PERT in the 1950s, and data-flow diagrams and IDEF in the 1970s. Among the modern methods are Unified Modeling Language and Business Process Model and Notation. The term business process modeling was coined in the 1960s in the field of systems engineering by S. Williams in his 1967 article "Business Process Modelling Improves Administrative Control". He proposed that techniques for obtaining a better understanding of physical control systems could be used in a similar way for business processes.
In the 1990s, the term process became a new productivity paradigm. Companies were encouraged to think in processes instead of functions and procedures. The traditional modeling tools were developed to illustrate time and cost, while modern tools focus on cross-functional activities. These cross-functional activities have increased significantly in number and importance, due to the growth of complexity and dependence. New methodologies include business process redesign, business process innovation, business process management, integrated business planning, among others.


== Objectives ==

The objective of business process modeling is a, usually graphical, representation of end-to-end processes, whereby complex processes are documented using a systematized representation. BPM typically begins with determining the environmental requirements: The goal of the modeling, the model addressees, and the business processes.
The qualities of the business process that are to be represented in the model are specified in accordance with the goal of the modeling. As a rule, these are not only the functions constituting the process, including the relationships between them, but also a number of other qualities, such as formal organization, input, output, resources, information, etc.
The objectives of business process modeling may include:

Documentation of the company's business processes
Definition of process performance indicators and monitoring of process performance
Preparation/Implementation of a business process optimization
Definition of interfaces and SLAs
Modularization of company processes
Benchmarking between parts of the company, partners, and competitors
Performing activity-based costing and simulations
Accompanying organizational changes


== Applications ==
There are a number of purposes as different applications for BPM:

Organizational documentation to increase the efficiency of communication about the processes
Process-oriented re-organization, for business process re-engineering, continual improvement process, and vulnerability assessment.
Continuous process management
Knowledge management to increase transparency about the company's knowledge resource
Software development, using the processes for the description of the requirements for software development
Workflow management
Simulation for investigating system behavior over time and identifying bottlenecks
ISO Certifications
Inter-company benchmarking
Process Optimization with techniques like Kaizen and Six Sigma


== Design Procedure ==


=== Analysis of business activities ===


==== Define framework conditions ====
The analysis of business activities determines and defines the framework conditions for successful business process modeling. Ideal steps can be:
define the relevant applications of business process modeling on the basis of the business model and where it is positioned in the value chain,
derive the strategy for the long-term success of business process modeling from the business strategy and develop an approach for structuring the business process models. Both the relevant purposes and the strategy directly influence the process map.


==== Identify business processes ====
A business process constitutes a set of interconnected, organized activities geared towards delivering a specific service or product for a particular clientele.


==== Structure business processes – building a process map ====
The structuring of business processes generally begins with a distinction between management, core, and support processes.

Management processes govern the operation of a company. Typical management processes include corporate governance and strategic management. They define corporate objectives and monitor the achievement of objectives.
Core processes constitute the core business and create the primary value stream. Typical operational processes are purchasing, manufacturing, marketing, and sales. They generate visible, direct customer benefits.
Support processes provide and manage operational resources. They support the core and management processes by ensuring the smooth running of business operations.  Examples include accounting, recruitment, and technical support.
Once the business processes have been identified and named, they can be compiled in overviews referred to as process maps. These can be represented through models like value chain diagrams.


=== Assigning the process responsibility ===
The process owner is responsible for success, creates the framework conditions, and coordinates approach with that of the other process owners, and is responsible for the exchange of information between the business processes. This coordination is necessary in order to achieve the overall goal orientation.


=== Modeling business process ===
As-is modeling and to-be modeling
The question of whether the business process model should be created through as-is modeling or to-be modeling is significantly influenced by the defined application and the strategy for the long-term success of business process modeling. The previous procedure with analysis of business activities, definition of business processes and further structuring of business processes is advisable in any case.

As-is modeling
Ansgar Schwegmann and Michael Laske state that as-is modeling helps in identifying weaknesses and localizing potential for improvement.
The following disadvantages speak against as-is modeling:

The creativity of those involved in the project to develop optimal target processes is stifled, as old structures and processes may be adopted without reflection in downstream target modeling.
The creation of detailed as-is models represents a considerable effort, also influenced by the effort required to reach a consensus between the project participants at interfaces and responsibility transitions.
To-be modeling
Mario Speck and Norbert Schnetgöke define the objective of to-be modeling as designing the target processes based on the strategic goals of the company. This involves analysing all sub-processes and individual activities of a company with regard to their target contribution.
They also list five basic principles that have proven their worth in the creation of the to-be models:

Parallel processing of sub-processes and individual activities is preferable to sequential processing – it contains the greater potential for optimization.
The development of a sub-process should be carried out as consistently as possible by one person or group – this allows the best model quality to be achieved.
Self-monitoring should be made possible for individual sub-processes and individual activities during processing – this reduces quality assurance costs.
If not otherwise possible, at least one internal customer/user should be defined for each process – this strengthens customer awareness and improves the assessability of process performance.
Learning effects that arise during the introduction of the target processes should be taken into account – this strengthens the employees' awareness of value creation.


==== Components ====
Components that can be used for modelling are:

Sub-processes
Functions or Tasks
Artifacts
External documents or IT systems


=== Model consolidation ===
For a successful model consolidation, it may be necessary to revise the original decomposition of the sub-processes and check for any redundancies.


=== Process chaining ===
The chaining of the sub-processes with each other and the chaining of the functions (tasks) in the sub-processes is modeled using Control Flow Patterns.


=== Process interfaces ===
Process interfaces are defined in order to

Show the relationships between the sub-processes after the decomposition of business processes
Determine what the business processes or their sub-processes must 'pass on' to each other
Process interfaces represent the exit from the current business process/sub-process and the entry into the subsequent business process/sub-process

Interfaces can be defined by:

Transfer of responsibility/accountability from one business unit to another
Transfer of data from one IT-system to another
In real terms, the transferred inputs/outputs are often data or information, but any other business objects are also conceivable.


== Representation type and notation ==


=== Modelling techniques ===
There are various standards for notations of BPM; the most common are:

Business Process Model and Notation (BPMN)
Event-driven process chain (EPC)
Value-added chain diagram (VAD), for visualizing processes mainly at a high level of abstraction
Petri net, developed by Carl Adam Petri in 1962
HIPO model, developed by IBM as a design aid and documentation technology for software
Lifecycle Modeling Language (LML)
Subject-oriented business process management (S-BPM)
Cognition enhanced Natural language Information Analysis Method (CogNIAM)
Unified Modelling Language (UML)
ICAM DEFinition (IDEF0), developed for the US Air Force in the early 1980s
Formalized Administrative Notation (FAN)
Harbarian process modeling (HPM)
Business Process Execution Language (BPEL), an XML-based language developed in 2002 by OASIS for the description and automation of business processes
Turtle diagram (also turtle method, turtle model, 8W method), a simple, clear and easy-to-understand graphical representation of facts about the process
Furthermore:

Communication structure analysis, proposed in 1989 by Prof. Hermann Krallmann at the Systems Analysis Department of the TU Berlin.
Extended Business Modelling Language (xBML)
Notation from OMEGA (object-oriented method for business process modeling and analysis), presented by Uta Fahrwinkel in 1995
Semantic object model (SOM)
PICTURE-Methode for the documentation and modeling of business processes in public administration
Data-flow diagram, a way of representing a flow of data through a process or a system
Swimlane technique, mainly known through BPMN and SIPOC
ProMet, a method set for business engineering
State diagram, used to describe the behavior of systems
In addition, representation types from software architecture can also be used:

Flowchart
Nassi-Shneiderman diagram or structure diagram


=== Tools ===
BPM tools provide business users with the ability to model their business processes, implement and execute those models, and refine the models based on as-executed data. As a result, business process modelling tools can provide transparency into business processes, as well as the centralization of corporate business process models and execution metrics. Modelling tools may also enable collaborative modelling of complex processes by users working in teams, where users can share and simulate models collaboratively. BPM tools should not be confused with business process automation systems – both practices have modeling the process as the same initial step and the difference is that process automation gives you an 'executable diagram' and that is drastically different from traditional graphical business process modelling tools.


==== Programming language tools ====
BPM suite software provides programming interfaces (web services, application program interfaces (APIs)) which allow enterprise applications to be built to leverage the BPM engine. This component is often referenced as the engine of the BPM suite.
Programming languages that are being introduced for BPM include:

Business Process Execution Language (BPEL)
Web Services Choreography Description Language (WS-CDL)
XML Process Definition Language (XPDL)
Some vendor-specific languages:

Architecture of Integrated Information Systems (ARIS) supports EPC
Java Process Definition Language (JBPM)
Other technologies related to business process modelling include model-driven architecture and service-oriented architecture.


==== Simulation ====
The simulation functionality of such tools allows for pre-execution modelling and simulation. Post-execution optimization is available based on the analysis of actual as-performed metrics.

Use case diagrams created by Ivar Jacobson, 1992 (integrated into UML)
Activity diagrams (also adopted by UML)


== See also ==

Business reference model
Business process re-engineering
Business process management
Business architecture
Business Model Canvas
Business plan
Business process mapping
Capability Maturity Model Integration
Drakon-chart
Generalised Enterprise Reference Architecture and Methodology
Model Driven Engineering
Outline of consulting
Value Stream Mapping


== References ==


== Further reading ==
Aguilar-Saven, Ruth Sara. "Business process modelling: Review and framework Archived 2020-08-07 at the Wayback Machine." International Journal of production economics 90.2 (2004): 129–149.
Barjis, Joseph (2008). "The importance of business process modeling in software systems design". Science of Computer Programming. 71: 73–87. doi:10.1016/j.scico.2008.01.002.
Becker, Jörg, Michael Rosemann, and Christoph von Uthmann. "Guidelines of business process modelling." Business Process Management. Springer Berlin Heidelberg, 2000. 30–49.
Hommes, L. J. The Evaluation of Business Process Modelling Techniques. Doctoral thesis. Technische Universiteit Delft.
Håvard D. Jørgensen (2004). Interactive Process Models. Thesis Norwegian University of Science and Technology Trondheim, Norway.
Manuel Laguna, Johan Marklund (2004). Business Process Modeling, Simulation, and Design. Pearson/Prentice Hall, 2004.
Ovidiu S. Noran (2000). Business Modelling: UML vs. IDEF Paper Griffh University
Jan Recker (2005). "Process Modelling in the 21st Century". In: BP Trends, May 2005.
Ryan K. L. Ko, Stephen S. G. Lee, Eng Wah Lee (2009) Business Process Management (BPM) Standards: A Survey. In: Business Process Management Journal, Emerald Group Publishing Limited. Volume 15 Issue 5. ISSN 1463-7154.
Jan Vanthienen, S. Goedertier and R. Haesen (2007). "EM-BrA2CE v0.1: A vocabulary and execution model for declarative business process modelling".  DTEW – KBI_0728.


== External links ==
 Media related to Business process modeling at Wikimedia Commons
