# Prototype JavaScript Framework

Cloned from https://en.wikipedia.org/wiki/Prototype_JavaScript_Framework.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 6189087.

The Prototype JavaScript Framework is a JavaScript framework created by Sam Stephenson in February 2005 as part of Ajax support in Ruby on Rails. It is implemented as a single file of JavaScript code, usually named prototype.js. Prototype is distributed standalone, but also as part of larger projects, such as Ruby on Rails, script.aculo.us and Rico. As of March 2021, according to w3techs, Prototype is used by 0.6% of all websites.


== Features ==
Prototype provides various functions for developing JavaScript applications. The features range from programming shortcuts to major functions for dealing with XMLHttpRequest.
Prototype also provides library functions to support classes and class-based objects. In JavaScript, object creation is prototype-based instead: an object creating function can have a prototype property, and any object assigned to that property will be used as a prototype for the objects created with that function. The Prototype framework is not to be confused with this language feature.


== Sample utility functions ==


=== The $() function ===
The dollar function, $(), can be used as shorthand for the getElementById function. To refer to an element in the Document Object Model (DOM) of an HTML page, the usual function identifying an element is:

The $() function reduces the code to:

The $() function can also receive an element as parameter and will return, as in the previous example, a prototype extended object.

Note: Like the underscore (_), the $ character is a legal "word character" in JavaScript identifiers, and has no other significance in the language. It was added to the language at the same time as support for regular expressions, so that the Perl-like matching variables could be emulated, such as $` and $'.


=== The $F() function ===
Building on the $() function: the $F() function returns the value of the requested form element. For a 'text' input, the function will return the data contained in the element. For a 'select' input element, the function will return the currently selected value.


=== The $$() function ===
The dollar dollar function is Prototype's CSS Selector Engine. It returns all matching elements, following the same rules as a selector in a CSS stylesheet. For example, if you want to get all <a> elements with the class "pulsate", you would use the following:

This returns a collection of elements. If you are using the script.aculo.us extension of the core Prototype library, you can apply the "pulsate" (blink) effect as follows:


=== The Ajax object ===
In an effort to reduce the amount of code needed to run a cross-browser XMLHttpRequest function, Prototype provides the Ajax object to abstract the different browsers. It has two main methods: Ajax.Request() and Ajax.Updater().
There are two forms of the Ajax object. Ajax.Request returns the raw XML output from an AJAX call, while the Ajax.Updater will inject the return inside a specified DOM object.
The Ajax.Request below finds the current values of two HTML form input elements, issues an HTTP POST request to the server with those element name/value pairs, and runs a custom function (called showResponse below) when the HTTP response is received from the server:


== Object-oriented programming ==
Prototype also adds support for more traditional object-oriented programming. The Class.create() method is used to create a new class. A class is then assigned a prototype which acts as a blueprint for instances of the class.

Extending another class:

The framework function Object.extend(dest, src) takes two objects as parameters and copies the properties of the second object to the first one simulating inheritance. The combined object is also returned as a result from the function. As in the example above, the first parameter usually creates the base object, while the second is an anonymous object used solely for defining additional properties. The entire sub-class declaration happens within the parentheses of the function call.


== Problems ==
Unlike other JavaScript libraries like jQuery, Prototype extends the DOM. There are plans to change this in the next major version of the library.
In April 2010, blogger Juriy 'kangax' Zaytsev (of Prototype Core) described at length the problems that can follow from monkey patching new methods and properties into the objects defined by the W3C DOM. These ideas echo thoughts published in March 2010 by Yahoo! developer Nicholas C. Zakas They have been summarized as follows

Cross browser issues: host objects are not subject to rules, non-compliant IE DOM behavior, etc.
Chance of name collisions
Performance overhead
By 2008, specific issues with using DOM-extension methods in older versions of Prototype, combined with newer versions of current browsers, were already being documented. Rather than adding new methods and properties to pre-existing 'host' DOM objects such as Element, like element.hide(), the solution to these issues is to provide wrapper objects around these host objects and implement the new methods on these. jQuery is such a wrapper object in the library of that name.


== See also ==

Ajax (programming)
Comparison of JavaScript frameworks
Mootools JavaScript Framework
jQuery
JavaScript framework
JavaScript library


== References ==


== Bibliography ==


== External links ==
Official website
