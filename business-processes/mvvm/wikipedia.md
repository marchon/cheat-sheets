# Model–view–viewmodel

Cloned from https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 23070896.

Model–view–viewmodel (MVVM) is a layer architecture design in computer software that facilitates the separation of the development of a graphical user interface (GUI; the view)—be it via a markup language or GUI code—from the development of the business logic or back-end logic (the model) such that the view is not dependent upon any specific model platform.
The viewmodel of MVVM is a value converter, meaning it is responsible for exposing (converting) the data objects from the model in such a way they can be easily managed and presented. In this respect, the viewmodel is more model than view, and handles most (if not all) of the view's display logic. The viewmodel may implement a mediator pattern, organizing access to the back-end logic around the set of use cases supported by the view.
MVVM is a variation of Martin Fowler's Presentation Model design pattern. MVVM is very similar to the Model-view-presenter pattern.  It was invented by Microsoft architects Ken Cooper and Ted Peters specifically to simplify event-driven programming of user interfaces. The pattern was incorporated into the Windows Presentation Foundation (WPF) (Microsoft's .NET graphics system) and Silverlight, WPF's Internet application derivative. John Gossman, a Microsoft WPF and Silverlight architect, announced MVVM on his blog in 2005.
Model–view–viewmodel is also referred to as model–view–binder, especially in implementations not involving the .NET platform. ZK, a web application framework written in Java, and the JavaScript library KnockoutJS use model–view–binder.


== Components of MVVM pattern ==
Model
Model refers either to a domain model, which represents real state content (an object-oriented approach), or to the data access layer, which represents content (a data-centric approach).
View
As in the model–view–controller (MVC) and model–view–presenter (MVP) patterns, the view is the structure, layout, and appearance of what a user sees on the screen. It displays a representation of the model and receives the user's interaction with the view (mouse clicks, keyboard input, screen tap gestures, etc.), and it forwards the handling of these to the view model via the data binding (properties, event callbacks, etc.) that is defined to link the view and view model.
View model
The view model is an abstraction of the view exposing public properties and commands. Instead of the controller of the MVC pattern, or the presenter of the MVP pattern, MVVM has a binder, which automates communication between the view and its bound properties in the view model. The view model has been described as a state of the data in the model.
The main difference between the view model and the Presenter in the MVP pattern is that the presenter has a reference to a view, whereas the view model does not. Instead, a view directly binds to properties on the view model to send and receive updates. To function efficiently, this requires a binding technology or generating boilerplate code to do the binding.

Binder
Declarative data and command-binding are implicit in the MVVM pattern. In the Microsoft solution stack, the binder is a markup language called XAML. The binder frees the developer from being obliged to write boiler-plate logic to synchronize the view model and view. When implemented outside of the Microsoft stack, the presence of a declarative data binding technology is what makes this pattern possible, and without a binder, one would typically use MVP or MVC instead and have to write more boilerplate (or generate it with some other tool).


== Rationale ==
MVVM was designed to remove virtually all GUI code ("code-behind") from the view layer, by using data binding functions in WPF (Windows Presentation Foundation) to better facilitate the separation of view layer development from the rest of the pattern. Instead of requiring user experience (UX) developers to write GUI code, they can use the framework markup language (e.g. XAML) and create data bindings to the view model, which is written and maintained by application developers. The separation of roles allows interactive designers to focus on UX needs rather than programming of business logic. The layers of an application can thus be developed in multiple work streams for higher productivity. Even when a single developer works on the entire codebase, a proper separation of the view from the model is more productive, as the user interface typically changes frequently and late in the development cycle based on end-user feedback.
The MVVM pattern attempts to gain both advantages of separation of functional development provided by MVC, while leveraging the advantages of data bindings and the framework by binding data as close to the pure application model as possible. It uses the binder, view model, and any business layers' data-checking features to validate incoming data. The result is that the model and framework drive as much of the operations as possible, eliminating or minimizing application logic which directly manipulates the view (e.g., code-behind).


== Criticism ==
John Gossman has criticized the MVVM pattern and its application in specific uses, stating that MVVM can be "overkill" when creating simple user interfaces. For larger applications, he believes that generalizing the viewmodel upfront can be difficult, and that large-scale data binding can lead to lower performance.


== Implementations ==


=== .NET frameworks ===
.NET Community Toolkit
Avalonia
Caliburn, Caliburn.Micro
Chinook.DynamicMvvm Open source
DevExpress MVVM
DotVVM open source project
FreshMvvm
Jellyfish
Mugen MVVM Toolkit
MVVMLight Toolkit
MvvmCross
MvvmZero
Prism Library
Rascl
ReactiveUI
Uno Platform - Open source


==== Web Component libraries ====
Microsoft FAST
Omi.js


=== Java frameworks ===
ZK Studio


=== JavaScript frameworks ===
Angular
Aurelia
Durandal
Ember.js
Ext JS
Knockout.js
Oracle JET
React
Svelte
Vue.js


=== Frameworks for C++ and XAML (Windows) ===
C++/WinRT
Xamlcc


== Examples ==
The following are simple examples of an implementation of the MVVM pattern.


=== C++ ===
This is an example using C++.

Then, the application could be run like so:


=== C# ===
This is an example using C#.
Model.cs:

ViewModel.cs:

View.cs:

Then, the application Main.cs could be run like so:


=== Java ===
This is an example using Java.
Model.java:

ViewModel.java:

View.java:

Then, the application Main.java could be run like so:


=== Rust ===
This is an example using Rust.

Then, the application main.rs could be run like so:


== See also ==
Multitier architecture
Model–view–controller
Model–view–presenter


== References ==
