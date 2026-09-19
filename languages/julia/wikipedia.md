# Julia (programming language)

Cloned from https://en.wikipedia.org/wiki/Julia_(programming_language).

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 38455554.

Julia is a dynamic general-purpose programming language. As a high-level language, distinctive aspects of Julia's design include a type system with parametric polymorphism, the use of multiple dispatch as a core programming paradigm, just-in-time compilation and a parallel garbage collection implementation. Notably, Julia does not support classes with encapsulated methods but instead relies on the types of all of a function's arguments to determine which method will be called.
By default, Julia is run similarly to scripting languages, using its runtime, and allows for interactions, but Julia programs can also be compiled to small binary standalone executables (or to small libraries for e.g. Python), with e.g. the JuliaC.jl compiler. 
Julia programs can reuse libraries from other languages, and vice versa. Julia has interoperability with C, C++, Fortran, Rust, Python, and R. Additionally, some Julia packages have bindings to be used from Python and R as libraries.
Julia is supported by programmer tools like IDEs (see below) and by notebooks like Pluto.jl, Jupyter, and since 2025, Google Colab officially supports Julia natively.
Julia is sometimes used in embedded systems (e.g. has been used in a satellite in space on a Raspberry Pi Compute Module 4; 64-bit Pis work best with Julia, and Julia is supported in Raspbian).


== History ==
Work on Julia began in 2009, when Jeff Bezanson, Stefan Karpinski, Viral B. Shah, and Alan Edelman set out to create a free language that was both high-level and fast. On 14 February 2012, the team launched a website with a blog post explaining the language's mission. In an interview with InfoWorld in April 2012, Karpinski said about the name of the language, Julia: "There's no good reason, really. It just seemed like a pretty name." Jeff Bezanson said he chose the name on the recommendation of a friend, then years later wrote:

Maybe julia stands for "Jeff's uncommon lisp is automated"?
Julia's syntax has been stable since version 1.0 in 2018, has a backward compatibility guarantee for 1.x, and has a stability promise for the documented (stable) API. The registered package ecosystem uses the 1.x syntax, and in most cases relies on new APIs that have been added regularly.
In the 10 years since the 2012 launch of pre-1.0 Julia, the community has grown. The Julia package ecosystem has over 11.8 million lines of code (including docs and tests). The JuliaCon academic conference for Julia users and developers has been held annually since 2014 with JuliaCon2020 welcoming over 28,900 unique viewers, and then JuliaCon2021 breaking all previous records (with more than 300 JuliaCon2021 presentations available for free on YouTube, up from 162 the year before), and 43,000 unique viewers during the conference.
Three of the Julia co-creators are the recipients of the 2019 James H. Wilkinson Prize for Numerical Software (awarded every four years) "for the creation of Julia, an innovative environment for the creation of high-performance tools that enable the analysis and solution of computational science problems." Also, Alan Edelman, professor of applied mathematics at MIT, has been selected to receive the 2019 IEEE Computer Society Sidney Fernbach Award "for outstanding breakthroughs in high-performance computing, linear algebra, and computational science and for contributions to the Julia programming language."
Version 0.3 was released in August 2014. Both Julia 0.7 and version 1.0 were released on 8 August 2018.  Julia 1.4 added syntax for generic array indexing to handle e.g. 0-based arrays. The memory model was also changed. Julia 1.5 released in August 2020 added record and replay debugging support, for Mozilla's rr tool.  The release changed the behavior in the REPL (to soft scope) to the one used in Jupyter, but keeps full compatible with non-REPL code (that retains hard scope).  Julia 1.6 was the largest release since 1.0, and it was the long-term support (LTS) version for the longest time. Since Julia 1.7 development is back to time-based releases, and it was released in November 2021 with e.g. a new  default random-number generator and Julia 1.7.3 fixed at least one security issue. Julia 1.8  added options for hiding source code when compiling Julia source code to executables.  Julia 1.9  has  added the ability to precompile packages to native machine code, done automatically; to improve precompilation of packages a new package PrecompileTools.jl was introduced, for use by package developers. Julia 1.10 was released on 25 December 2023 with new features such as parallel garbage collection. Julia 1.11 was released on 7 October 2024, and with it 1.10.5 became the next long-term support (LTS) version (i.e. those became the only two supported versions), since replaced by 1.10.12 released on 16 August, and 1.6 is no longer an LTS version. Julia 1.11 adds e.g. the new public keyword to signal safe public API (Julia users are advised to use such API, not internals, of Julia or packages, and package authors advised to use the keyword, generally indirectly, e.g. prefixed with the @compat macro, from Compat.jl, to also support older Julia versions, at least the LTS version).
Julia 1.12 was released on 7 October 2025 (and 1.12.12 on 15 August 2026), and with it a JuliaC.jl package including the juliac compiler that works with it, for making rather small binary executables (much smaller than was possible before; through the use of the new so-called trimming feature). Julia 1.10 LTS is an officially still-supported branch, but the 1.11 branch has also been maintained after 1.12 release, with 1.11.8 released and then 1.11.9 released on 8 February 2026. Julia 1.13.0-rc4 is out, available as download, e.g. with juliaup.


=== JuliaCon ===
Since 2014, the Julia Community has hosted an annual Julia Conference focused on developers and users. The first JuliaCon took place in Chicago and kickstarted the annual occurrence of the conference. Since 2014, the conference has taken place across a number of locations including MIT and the University of Maryland, Baltimore. The event audience has grown from a few dozen people to over 28,900 unique attendees during JuliaCon 2020, which took place virtually. JuliaCon 2021 also took place virtually with keynote addresses from professors William Kahan, the primary architect of the IEEE 754 floating-point standard (which virtually all CPUs and languages, including Julia, use), Jan Vitek, Xiaoye Sherry Li, and Soumith Chintala, a co-creator of PyTorch. JuliaCon grew to 43,000 unique attendees and more than 300 presentations (still freely accessible, plus for older years). JuliaCon 2022 will also be virtual held between July 27 and July 29, 2022, for the first time in several languages, not just in English.


=== Sponsors ===
The Julia language became a NumFOCUS fiscally sponsored project in 2014 in an effort to ensure the project's long-term sustainability. Jeremy Kepner at MIT Lincoln Laboratory was the founding sponsor of the Julia project in its early days. In addition, funds from the Gordon and Betty Moore Foundation, the Alfred P. Sloan Foundation, Intel, and agencies such as NSF, DARPA, NIH, NASA, and FAA have been essential to the development of Julia. Mozilla, the maker of Firefox web browser, with its research grants for H1 2019, sponsored "a member of the official Julia team" for the project "Bringing Julia to the Browser", meaning to Firefox  and other web browsers. The Julia language is also supported by individual donors on GitHub.


=== JuliaHub ===
JuliaHub, Inc. was founded in 2015 as Julia Computing, Inc. by Viral B. Shah, Deepak Vinchhi, Alan Edelman, Jeff Bezanson, Stefan Karpinski and Keno Fischer.
In June 2017, Julia Computing raised US$4.6 million in seed funding from General Catalyst and Founder Collective, the same month was "granted $910,000 by the Alfred P. Sloan Foundation to support open-source Julia development, including $160,000 to promote diversity in the Julia community", and in December 2019 the company got $1.1 million funding from the US government to "develop a neural component machine learning tool to reduce the total energy consumption of heating, ventilation, and air conditioning (HVAC) systems in buildings". In July 2021, Julia Computing announced they raised a $24 million Series A round led by Dorilton Ventures, which also owns Formula One team Williams Racing, that partnered with Julia Computing. Williams' Commercial Director said: "Investing in companies building best-in-class cloud technology is a strategic focus for Dorilton and Julia's versatile platform, with revolutionary capabilities in simulation and modelling, is hugely relevant to our business. We look forward to embedding Julia Computing in the world's most technologically advanced sport". In June 2023, JuliaHub received (again, now under its new name) a $13 million strategic new investment led by AE Industrial Partners HorizonX ("AEI HorizonX"). AEI HorizonX is a venture capital investment platform formed in partnership with The Boeing Company, which uses Julia. Tim Holy's work (at Washington University in St. Louis's Holy Lab) on Julia 1.9 (improving responsiveness) was funded by the Chan Zuckerberg Initiative.


== Language features ==

Julia is a general-purpose programming language, while also originally designed for numerical/technical computing. It is also useful for low-level systems programming, as a specification language, high-level synthesis (HLS) tool (for hardware, e.g. FPGAs), and for web programming at both server and client side.
The main features of the language are:

Multiple dispatch: providing ability to define function behavior across combinations of argument types
Dynamic type system: types for documentation, optimization, and dispatch
Performance approaching that of statically typed languages like C
A built-in package manager
Lisp-like macros and other metaprogramming facilities
Designed for parallel and distributed computing
Coroutines: lightweight green threading
Automatic generation of code for different argument types
Extensible conversions and promotions for numeric and other types
Multiple dispatch (also termed multimethods in Lisp; though they're slower, most languages do not have an optimized implementation) is a generalization of single dispatch –  the polymorphic mechanism used in common object-oriented programming (OOP) languages, such as Python, C++, Java, JavaScript, and Smalltalk –  that use inheritance.
In Julia, all concrete types are subtypes of abstract types, directly or indirectly subtypes of the Any type, which is the top of the type hierarchy. Concrete types cannot themselves be subtyped the way they can in other languages; composition is used instead (see also inheritance vs subtyping).
By default, the Julia runtime must be pre-installed as user-provided source code is run. Alternatively, Julia (GUI) apps can be quickly bundled up into a single file with AppBundler.jl for "building Julia GUI applications in modern desktop application installer formats. It uses Snap for Linux, App Installer for Windows, and DMG for MacOS as targets. It bundles full Julia within the app". JuliaC and/or PackageCompiler.jl can build standalone executables that need no Julia source code to run.

In Julia, everything is an object, much like object-oriented languages; however, unlike most object-oriented languages, all functions use multiple dispatch to select methods, rather than single dispatch.
Most programming paradigms can be implemented using Julia's homoiconic macros and packages. Julia's syntactic macros (used for metaprogramming), like Lisp macros, are more powerful than text-substitution macros used in the preprocessor of some other languages such as C, because they work at the level of abstract syntax trees (ASTs). Julia's macro system is hygienic, but also supports deliberate capture when desired (like for anaphoric macros) using the esc construct.
Julia draws inspiration from various dialects of Lisp, including Scheme and Common Lisp, and it shares many features with Dylan, also a multiple-dispatch-oriented dynamic language (which features an infix syntax rather than a Lisp-like prefix syntax, while in Julia "everything" is an expression), and with Fortress, another numerical programming language (which features multiple dispatch and a sophisticated parametric type system). While Common Lisp Object System (CLOS) adds multiple dispatch to Common Lisp, not all functions are generic functions.
In Julia, Dylan, and Fortress, extensibility is the default, and the system's built-in functions are all generic and extensible. In Dylan, multiple dispatch is as fundamental as it is in Julia: all user-defined functions and even basic built-in operations like + are generic. Dylan's type system, however, does not fully support parametric types, which are more typical of the ML lineage of languages. By default, CLOS does not allow for dispatch on Common Lisp's parametric types; such extended dispatch semantics can only be added as an extension through the CLOS Metaobject Protocol. By convergent design, Fortress also features multiple dispatch on parametric types; unlike Julia, however, Fortress is statically rather than dynamically typed, with separate compiling and executing phases. The language features are summarized in the following table:

An example of the extensibility of Julia, the Unitful.jl package adds support for physical units of measurement to the language.


=== Interoperability ===
Julia has built-in support for calling C or Fortran  language libraries using the @ccall macro. Additional libraries allow users to call to or from other languages such as Python, C++, Rust, R, Java and to use with SQL.


=== Separately-compiled executables option ===
Julia can be compiled to binary executables with PackageCompiler.jl (or with juliac). Smaller executables can also be written using a static subset of the language provided by StaticCompiler.jl that does not support runtime dispatch (nor garbage collection, since excludes the runtime that provides it).


== Interaction ==
The Julia official distribution includes an interactive (optionally color-coded) read–eval–print loop (REPL; "command-line"), with a searchable history, tab completion, and dedicated help and shell modes, which can be used to experiment and test code quickly. The following fragment represents a sample session example where strings are concatenated automatically by println:

Since Unicode is supported, including for variables and functions you can for example define the Riemann xi function as follows:

Due to its lack of readability and support from some editors, the use of these symbols are controversial, as users may believe their use is mandatory. This perception forces developers to use the corresponding Unicode/Greek letters, especially in essential packages. One example of this is gamma function, defined by the package with the ASCII symbol. The example code shows both the symbol and its alias can be used; keyword arguments can be defined with ASCII or be defined with Greek or Unicode symbols. It's recommended to define aliases for all ASCII symbol in registered packages if possible.
The REPL gives user access to the system shell and to help mode, by pressing ; or ? after the prompt (preceding each command), respectively. It also keeps the history of commands, including between sessions. Code can be tested inside Julia's interactive session or saved into a file (with the idiomatic .jl extension considered best) and run from the command line by typing:

Julia uses UTF-8 and LaTeX codes, allowing it to support common math symbols for many operators, such as ∈ for the in operator, typable with \in then pressing Tab ↹ (i.e. uses LaTeX codes, or also possible by simply copy-pasting, e.g. √ and ∛ possible for sqrt and cbrt functions). Julia 12.x has supports Unicode 16 (Julia 1.13.0-rc3 supports latest 17.0 release and will support subscript q letter, probably first programming language to do so<;-- and The character U+1F8B2 🢲 (RIGHTWARDS ARROW WITH LOWER HOOK), newly added by Unicode 16, is now a valid operator with arrow precedence, accessible as \hookunderrightarrow at the REPL -->) for the languages of the world, even for source code, e.g. variable names (while it's recommended to use English for public code, and e.g. package names).
Julia is supported by Jupyter, an online interactive "notebooks" environment, and Pluto.jl, a "reactive notebook" (where notebooks are saved as pure Julia files), a possible replacement for the former kind. In addition Posit's (formerly RStudio Inc's) Quarto publishing system supports Julia, Python, R and Observable JavaScript (those languages have official support by the company, and can even be weaved together in the same notebook document, more languages are unofficially supported).
The REPL can be extended with additional modes, and has been with packages, e.g. with an SQL mode, for database access, and RCall.jl adds an R mode, to work with the R language.
Julia's Visual Studio Code extension provides a fully featured integrated development environment with "built-in dynamic autocompletion, inline results, plot pane, integrated REPL, variable view, code navigation, and many other advanced language features" e.g. debugging is possible, linting, and profiling.


=== Use with other languages ===
Julia is in practice interoperable with other languages, in fact the majority of the top 20 languages in popular use. Julia can be used to call shared library functions individually, such as those written in C or Fortran, and packages are available to allow calling other languages (which do not provide C-exported functions directly), e.g. Python (with PythonCall.jl), R, MATLAB, C# (and other .NET languages with DotNET.jl, from them with JdotNET), JavaScript, Java (and other JVM languages, such as Scala with JavaCall.jl). And packages for other languages allow to call to Julia, e.g. from Python, R, Rust, Ruby, or C#. Such as with juliacall (part of PythonCall.jl) to call from Python and a different JuliaCall package for calling from R. Julia has also been used for hardware, i.e. to compile to VHDL, as a high-level synthesis tool, for example FPGAs.
Julia has packages supporting markup languages such as HTML (and also for HTTP), XML, JSON and BSON, and for databases (such as PostgreSQL, Mongo, Oracle, including for TimesTen, MySQL, SQLite, Microsoft SQL Server, Amazon Redshift, Vertica, ODBC) and web use in general.


== Package system ==
Julia has a built-in package manager and includes a default registry system. Packages are most often distributed as source code hosted on GitHub, though alternatives can also be used just as well. Packages can also be installed as binaries, using artifacts. Julia's package manager is used to query and compile packages, as well as managing environments. Federated package registries are supported, allowing registries other than the official to be added locally.


== Implementation ==
Julia's core is implemented in Julia and C, together with C++ for the LLVM dependency. The code parsing, were implemented in FemtoLisp, a Scheme dialect, up to version 1.10. Since that version the new pure-Julia stdlib  JuliaSyntax.jl is used for the parsing (while the old one can still be chosen) which improves speed and "greatly improves parser error messages in various cases". The bootstrapping is still using FemtoLisp. The LLVM compiler infrastructure project is used as the back end for generating optimized machine code for all commonly used platforms. With some exceptions, the standard library is implemented in Julia. Julia has supported for expected machine integers from Int8 up to Int128 (and unsigned versions), and Rationals of such and BigInt and BigFloat, and Float64 down to Float16 (as a storage format), but also separately has minimal support for BFloat16 with the main support in packages like BFloat16.jl. Support for other types, such as decimal floating point or smaller or other alternative types lives in packages, like DecFP.jl, Float8s.jl, MultiFloat.jl, BPosits.jl and UniversalNumbers.jl. Julia supports complex numbers of all the number types.


=== Current and future platforms ===
Julia has four support tiers, for reference see Julia's official support table.
As of June 2026 Julia has Tier 1 (complete) support for 32- and 64-bit Windows and Linux, as well as MacOS (both x64 Intel and Apple Silicon natively); Tier 2 support (builds, may fail some tests) for ARM64 on both Windows and Linux, FreeBSD, and emulation such as WSL 2 and x86-on-Arm; Tier 3 support (may build) for exotic architectures, such as RISC-V, PowerPC, and Linux musl; and Tier 4 (former) support for ARM32.  Julia also supports hardware accelerators through external packages, with official tiers: NVidia CUDA on 64-bit Linux (Tier 1), CUDA on 64-bit Windows, Apple Metal for 64-bit Arm-based macOS (Tier 2), and Intel oneAPI on 64-bit Linux (Tier 2), and AMD ROCm and Intel OneAPI on 64-bit Windows (Tier 3). Multi-threading is supported natively.
Julia has been built for several ARM platforms, from small Raspberry Pis up to then world's fastest supercomputer Fugaku's ARM-based A64FX (fastest in 2020, another ARM-based became fastest in 2026, Julia should run on all the fastest supercomputers). 
Julia has official (tier 2) support for 64-bit ARMv8 meaning e.g. newer 64-bit (ARMv8-A) Raspberry Pi computers work with Julia (e.g. the Pi Compute Module 4 has been used in space running Julia code). For many Pis, especially older 32-bit ones, it helps to cross-compile the user's Julia code for them. The older 32-bit ARMv7 Pis worked in older Julia versions (still do, but for latest Julia version(s), note downgraded from tier 3 to its current tier 4: "Julia built at some point in the past, but is known not to build currently."). The original Raspberry Pi 1 has no official support (since it uses ARMv6 which has newer had a support tier; though some cut-down Julia  has been known to run on that Pi).
Pico versions of the Pi are known to no work (since using the M-profile Arm, not running under Linux; not yet supported). Julia is now supported in Raspbian while support is better for newer Pis, e.g., those with Armv7 or newer; the Julia support is promoted by the Raspberry Pi Foundation.
On some platforms, Julia may need to be compiled from source code (e.g., the original Raspberry Pi), with specific build options, which has been done and unofficial pre-built binaries (and build instructions) are available.
Julia has also been built for 64-bit RISC-V (has tier 3 support), i.e. has some supporting code in core Julia.
While Julia requires an operating system by default, and has no official support to run without, or on embedded system platforms such as Arduino, Julia code has still been run on it, with some limitations, i.e. on a baremetal 16 MHz 8-bit (ATmega328P) AVR-microcontroller Arduino with 2 KB RAM (plus 32 KB of flash memory).


== Adoption ==
Julia has been adopted at many universities including MIT, Stanford, UC Berkeley, Technical University of Munich, Ferdowsi University of Mashhad and the University of Cape Town. Large private firms across many sectors have adopted the language including Amazon, IBM, JP Morgan AI Research, and ASML. Julia has also been used by government agencies including NASA and the FAA, as well as every US national energy laboratory.


=== Scientific computing and engineering ===
Amazon, for quantum computing and machine learning through Amazon SageMaker
ASML, for hard real-time programming with their machines
The Climate Modeling Alliance for climate change modeling
CERN, to analyze data from the Large Hadron Collider (LHCb experiment)
NASA and the Jet Propulsion Laboratory use Julia to model spacecraft separation dynamics, analyze TRAPPIST exoplanet datasets, and analyze cosmic microwave background data from the Big Bang
The Brazilian INPE, for space missions and satellite simulations
Julia has also flown in space, on a small  satellite, used for a GPS module. And Julia has also been used to design satellite constellations.
Embedded hardware to plan and execute flight of autonomous U.S. Air Force Research Laboratory VTOL drones


==== Pharmaceuticals and drug development ====
Julia is widely used for drug development in the pharmaceutical industry, having been adopted by Moderna, Pfizer, AstraZeneca, Procter & Gamble, and United Therapeutics.


=== Economics, finance, and political science ===
The Federal Reserve Bank of New York have used Julia for macroeconomic modeling since 2015, including estimates of COVID-19 shocks in 2021
Also the Bank of Canada, central bank, for macroeconomic modeling
BlackRock, the world's largest asset manager, for financial time-series analysis
Aviva, the UK's largest general insurer, for actuarial calculations
Mitre Corporation, for verification of published election results
Nobel laureate Thomas J. Sargent, for macroeconometric modeling


== See also ==

Comparison of statistical packages
Differentiable programming
JuMP – an algebraic modeling language for mathematical optimization embedded in Julia
List of Julia software and tools
Python
Mojo
Nim


== References ==


== External links ==
Julia documentation


== Further reading ==
Nagar, Sandeep (2017). Beginning Julia Programming: For Engineers and Scientists. Springer. ISBN 978-1-4842-3171-5.
Bezanson, J; Edelman, A; Karpinski, S; Shah, V. B (2017). "Julia: A fresh approach to numerical computing". SIAM Review. 59 (1): 65–98. arXiv:1411.1607. doi:10.1137/141000671. S2CID 13026838.
Joshi, Anshul (2016). Julia for Data Science － Explore the world of data science from scratch with Julia by your side. Packt. ISBN 978-1-78355-386-0.
Tobin A Driscoll and Richard J. Braun (Aug. 2022). Fundamentals of Numerical Computation: Julia Edition. SIAM. ISBN 978-1-611977-00-4.
C. T. Kelley (2022). Solving Nonlinear Equations with Iterative Methods: Solvers and Examples in Julia, SIAM. ISBN 978-1-611977-26-4.
Kalicharan, Noel (2021). Julia - Bit by Bit. Undergraduate Topics in Computer Science. Springer. doi:10.1007/978-3-030-73936-2. ISBN 978-3-030-73936-2. S2CID 235917112.
Clemens Heitzinger (2022): Algorithms with Julia, Springer, ISBN 978-3-031-16559-7.
Kenneth Lange (Jun. 2025): Algorithms from THE BOOK (2nd Ed.), SIAM, ISBN 978-1-61197-838-4.


== External links ==

Official website
https://juliahub.com
Julia on GitHub
