# OpenSCAD

Cloned from https://en.wikipedia.org/wiki/OpenSCAD.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 25778048.

OpenSCAD is a free software application for creating solid 3D computer-aided design (CAD) objects. It is a script-only based modeller that uses its own description language; the 3D preview can be manipulated interactively, but cannot be interactively modified in 3D. Instead, an OpenSCAD script specifies geometric primitives (such as spheres, boxes, cylinders, etc.) and defines how they are modified and combined (for instance by intersection, difference, envelope combination, or Minkowski sums) to render a 3D model. As such, the program performs constructive solid geometry (CSG). OpenSCAD is available for Windows, Linux, and macOS.


== Overview ==


=== Scripting language ===
OpenSCAD uses a custom scripting language to produce 3D graphics. The scripting language supports functional programming, parametrized modularization and reuse, and mathematical computation. Variables are scoped, but within each scope are immutable.


=== Previewing ===
For fast previewing of models using z-buffering, OpenSCAD employs OpenCSG and OpenGL.
The 3D model position can be interactively manipulated in the view with a mouse similarly to other 3D modellers. It is also possible to define a default "camera" position in the script.
Part colors can be defined in the 3D view (including transparency).
Preview is relatively fast and allows interactive modifications while modifying the script.
The model renderer takes into account lighting, but the lighting source is not modifiable.


== Use ==
OpenSCAD allows a designer to create accurate 3D models and parametric designs that can be easily adjusted by changing the parameters.
OpenSCAD documents are human-readable scripts in plain ASCII text and potentially syntactically better suited to integrate with version control systems such as git.
As such, OpenSCAD is a programmer-oriented solid-modeling tool and has been recommended as an entry-level CAD tool for designing open-source hardware such as scientific tools for research and education.
It is often used to design 3D printed parts, which can be exported in various 3D file formats. Its script-based parametric nature allows it to be integrated into online model customization services, such as the "Customizer" tool on Thingiverse.

Animation is possible with a speed of a few images per seconds for simple models. The animation can have effect on any parameter, being it the camera position or the parts dimensions, position, shape or existence. It can be recorded as a set of images usable to build animated GIFs.
An experimental coupling with Calculix for FEM (Finite Element Method) is available.
FreeCAD can import OpenSCAD files also for FEM with Calculix or other supported FEM solvers. FreeCAD features a workbench for interoperability with OpenSCAD.
Tools also exist to generate OpenSCAD code from higher-level inputs; for example, CADAM is an open-source text-to-CAD web application that converts natural-language prompts into parametric OpenSCAD scripts.


== File formats ==


=== Imports ===
2D drawings in DXF, SVG and PNG can be imported, then extruded as monolithic parts.
3D parts can be imported in STL, OFF, AMF and 3MF and can be scaled and submitted to subtractive or additive operations.


=== Exports ===
OpenSCAD views and models can be exported to many different formats. Including:

Views: can be exported in PNG format.
2D models can be exported in SVG, AutoCAD DXF, and PDF.
3D parts can be exported in 3MF, AMF, OFF, and STL as simple volumes. There is no color, material, or parts definition in the exported model.


== Design ==
OpenSCAD is a wrapper to a CSG engine with a graphical user interface and integrated editor, developed in C++. As of 2024, the general release version uses the Computational Geometry Algorithms Library (CGAL) as its basic CSG engine. However, development snapshot versions also offer support for Manifold as an alternative.
Its script syntax reflects a functional programming philosophy. Much as in Haskell, within a scope each "variable" is treated as a constant, immutable with at most one value.


== Platform implementations ==
Official standalone version written in C++ for Windows, MacOS, and Linux
FreeCAD: has an OpenSCAD command line interface that can be used instead of the part solver or part workbench
Browser implementations are also available, such as cadhub.xyz and jscad.app.


== See also ==

Comparison of computer-aided design software
PLaSM: another open source scripting language for creating 3D objects.


== References ==


== External links ==

Official website
openscad on GitHub
Primary IRC Chat
