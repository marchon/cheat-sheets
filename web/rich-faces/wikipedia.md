# RichFaces

Cloned from https://en.wikipedia.org/wiki/RichFaces.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 17765880.

RichFaces was an open source Ajax-enabled component library for JavaServer Faces, hosted by JBoss.  It allows easy integration of Ajax capabilities into enterprise application development. It reached its end-of-life in June 2016.
RichFaces is more than just a component library for JavaServer Faces. It adds:

Skinability (easily change and update application look and feel)
Component Development Kit (CDK) to assist in constructing JavaServer Faces components
Dynamic Resource Framework
Both page wide, and component based Ajax control components.


== History ==

RichFaces originated from the Ajax4jsf framework which Alexander Smirnov designed and implemented. In the autumn of 2005 Smirnov joined Exadel and continued to develop the framework. In March 2006 Exadel released the first version of what would become Ajax4jsf. Later in the same year, Exadel VCP was split off and the Ajax4jsf framework and RichFaces was born. While RichFaces provided out-of-the-box components (a "component-centric" Ajax approach, where components do everything you need), Ajax4jsf provided page-wide Ajax support. Developers specify which parts of the page the server should process after some client-side user actions and which parts should be updated after processing. Ajax4jsf became an open-source project hosted on java.net, while RichFaces became a commercial JSF component library.
In March 2007 JBoss (a division of Red Hat from 2006) and Exadel signed a partnership agreement whereby Ajax4jsf and RichFaces would come under the JBoss umbrella as "JBoss Ajax4jsf" and as "JBoss RichFaces". RichFaces would now also become open-source and free. In September 2007 JBoss and Exadel decided to merge Ajax4jsf and RichFaces under the RichFaces name. It made sense as both libraries were now free and open-source. Having just one product solved many existing version- and compatibility-issues, such as which version of Ajax4jsf would work with which version of RichFaces.
On February 12, 2016, the RichFaces developer Michal Petrov announced the end-of-life of RichFaces  for June 2016.


== Framework ==
The framework is implemented as a component library which adds Ajax capability into existing pages, so a developer doesn't need to write any JavaScript code or to replace existing components with new Ajax widgets. RichFaces enables page-wide Ajax support instead of the traditional component-wide support. Hence, a developer can define the event on the page that invokes an Ajax request and the areas of the page that should be synchronized with the JSF Component Tree after the Ajax request changes the data on the server according to the events fired on the client.
RichFaces allows you to define (by means of JSF tags) different parts of a JSF page you wish to update with an Ajax request, and provides a few options to send Ajax requests to the server. Also the JSF page doesn't change from a "regular" JSF page and you don't need to write any JavaScript code by hand. By controlling everything from the server side, almost no JavaScript is needed and the page state can be maintained easily in the server.


== RichFaces architecture ==
The architecture of RichFaces consists of an Ajax filter, Ajax action components, Ajax containers, and a JavaScript engine.

Ajax filter - In order to get all benefits of RichFaces, a developer should register a filter in the web.xml file of the application. The filter recognizes multiple request types.
Ajax action components - AjaxCommandButton, AjaxCommandLink, AjaxPoll and AjaxSupport and other action components can be used to send Ajax requests from the client side.
Ajax's containers - AjaxContainer is an interface that describes an area on a JSF page that should be decoded during an Ajax request. AjaxViewRoot and AjaxRegion are implementations of this interface.
JavaScript engine - the RichFaces JavaScript engine runs on the client-side. It updates different areas on a JSF page based on the information from the Ajax response. The JavaScript engine provides an API, so developers do not need to create their own JavaScript functionality.


== Skinnability ==
Skinnability is a special feature of RichFaces that is used for defining common interface styles. The feature is based on XCSS technology, which provides flexibility and dynamics.  RichFaces provides a set of predefined skins:

DEFAULT
plain
emeraldTown
blueSky
wine
japanCherry
ruby
classic
deepMarine
Laguna (new - RichFaces 3.2.1)
GlassX (new - RichFaces 3.2.2)
DarkX (new - RichFaces 3.2.2)
Skin properties, such as, generalBackgroundColor, generalLinkColor, headerFamilyFont etc. are stored in skinname.skin.properties file. Each component has a XCSS (a special file format that combines flexibility of XML and CSS) file that performs mapping of CSS selectors to the skin properties of a particular skin.  Additionally, RichFaces provides skinning for standard HTML controls.
You can create a custom skin using Plug-n-Skin feature, which is a Maven archetype that builds a skeleton for a new skin.


== Simple JSF page with RichFaces calendar component ==

This is the result of the presented above code


== See also ==

Comparison of web frameworks
List of JBoss software


== References ==


== External links ==
Official website
RichFaces Showcase
