# Document type declaration

Cloned from https://en.wikipedia.org/wiki/Document_type_declaration.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 40042954.

A document type declaration, or DOCTYPE, is an instruction that associates a particular XML or SGML document (for example, a web page) with a document type definition (DTD) (for example, the formal definition of a particular version of HTML 2.0 - 4.0). In the serialized form of the document, it manifests as a short string of markup that conforms to a particular syntax.
The HTML layout engines in modern web browsers perform DOCTYPE "sniffing" or "switching", wherein the DOCTYPE in a document served as text/html determines a layout mode, such as "quirks mode" or "standards mode". The text/html serialization of HTML5, which is not SGML-based, uses the DOCTYPE only for mode selection.  Since web browsers are implemented with special-purpose HTML parsers, rather than general-purpose DTD-based parsers, they do not use DTDs and never access them even if a URL is provided.  The DOCTYPE is retained in HTML5 as a "mostly useless, but required" header only to trigger "standards mode" in common browsers.


== Syntax ==
The general syntax for a document type declaration is:

or


=== Document type name ===
The opening <!DOCTYPE syntax is followed by separating syntax (such as spaces, or (except in XML) comments opened and closed by a doubled ASCII hyphen), followed by a document type name (i.e. the name of the root element that the DTD applies to trees descending from). In XML, the root element that represents the document is the first element in the document. For example, in XHTML, the root element is <html>, being the first element opened (after the doctype declaration) and last closed.
Since the syntax for the external identifier and internal subset are both optional, the document type name is the only information which it is mandatory to give in a DOCTYPE declaration.


=== External identifier ===
The DOCTYPE declaration can optionally contain an external identifier, following the root element name (and separating syntax such as spaces), but before any internal subset. This begins with either the keyword SYSTEM or the keyword PUBLIC, specifying whether the DTD is specified using a public identifier identifying it as a public text, i.e. one shared between multiple computer systems (regardless of whether it is an available public text available to the general public, or an unavailable public text shared only within an organisation). If the PUBLIC keyword is used, it is followed by the public identifier enclosed in double or single ASCII quotation marks. The public identifier does not point to a storage location, but is rather a unique fixed string intended to be looked up in a table (such as an SGML catalog); however, in some (but not all) SGML profiles, the public identifier must be constructed using a particular syntax called Formal Public Identifier (FPI), which specifies the owner as well as whether it is available to the general public.
The public identifier (if present) or SYSTEM keyword (otherwise) may (and, in XML, must) be followed by a "system identifier" that is likewise enclosed in quotation marks. Although the interpretation of system identifiers in general SGML is entirely system-dependent (and might be a filename, database key, offset, or something else), XML requires that they be URIs. For example, the FPI for XHTML 1.1 is "-//W3C//DTD XHTML 1.1//EN" and, there are 3 possible system identifiers available for XHTML 1.1 depending on the needs. One of them is the URL reference "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd". It means that the XML parser must locate the DTD in a system specific fashion, in this case, by means of a URL reference of the DTD enclosed in double quote marks. 
In XHTML documents, the doctype declaration must always explicitly specify a system identifier. In SGML-based documents like HTML, on the other hand, the appropriate system identifier may automatically be inferred from the given public identifier. This association might e.g. be performed by means of a catalog file resolving the FPI to a system identifier. The SYSTEM keyword can (except in XML) also be used without a system identifier following, indicating that a DTD exists but should be inferred from the document type name.


=== Internal subset ===
The last, optional, part of a DOCTYPE declaration is surrounded by literal square brackets ([]), and called an internal subset. It can be used to add/edit entities or add/edit PUBLIC keyword behaviors. It is possible, but uncommon, to include the entire DTD in-line in the document, within the internal subset, rather than referencing it from an external file. Conversely, the internal subset is sometimes forbidden within simple SGML profiles, notably those for basic HTML parsers that don't implement a full SGML parser.
If both an internal DTD subset and an external identifier are included in a DOCTYPE declaration, the internal subset is processed first, and the external DTD subset is treated as if it were transcluded at the end of the internal subset. Since earlier definitions take precedence over later definitions in a DTD, this allows the internal subset to override definitions in the external subset.


=== Example ===
The first line of a World Wide Web page may read as follows:

This document type declaration for XHTML includes by reference a DTD, whose public identifier is -//W3C//DTD XHTML 1.0 Transitional//EN and whose system identifier is http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd. An entity resolver may use either identifier for locating the referenced external entity. No internal subset has been indicated in this example or the next ones. The root element is declared to be html and, therefore, it is the first tag to be opened after the end of the doctype declaration in this example and the next ones, too. The HTML tag is not part of the doctype declaration but has been included in the examples for orientation purposes.


== Common DTDs ==
Some common DTDs have been put into lists. W3C has produced a list of DTDs commonly used in the web, which contains the "bare" HTML5 DTD, older XHTML/HTML DTDs, DTDs of common embedded XML-based formats like MathML and SVG as well as "compound" documents that combine those formats. Both W3C HTML5 and its corresponding WHATWG version recommend browsers to only accept XHTML DTDs of certain FPIs and to prefer using internal logic over fetching external DTD files. It further specifies an "internal DTD" for XHTML which is merely a list of HTML entity names.


=== HTML 4.01 DTDs ===
Strict DTD does not allow presentational markup with the argument that Cascading Style Sheets should be used for that instead. This is how the Strict DTD looks:

Transitional DTD allows some older  PUBLIC and attributes that have been deprecated:

If frames are used, the Frameset DTD must be used instead, like this:


=== XHTML 1.0 DTDs ===
XHTML's DTDs are also Strict, Transitional and Frameset.
XHTML Strict DTD. No deprecated tags are supported and the code must be written correctly according to XML Specification.

XHTML Transitional DTD is like the XHTML Strict DTD, but deprecated tags are allowed.

XHTML Frameset DTD is the only XHTML DTD that supports Frameset. The DTD is below.


=== XHTML 1.1 DTD ===
XHTML 1.1 is the most current finalized revision of XHTML, introducing support for XHTML Modularization. XHTML 1.1 has the stringency of XHTML 1.0 Strict.


=== XHTML Basic DTDs ===
XHTML Basic 1.0

XHTML Basic 1.1


=== HTML5 DTD-less DOCTYPE ===
HTML5 uses a DOCTYPE declaration which is very short, due to its lack of references to a DTD in the form of a URL or FPI. All it contains is the tag name of the root element of the document, HTML.  In the words of the specification draft itself:

<!DOCTYPE html>, case-insensitively.
With the exception of the lack of a URI or the FPI string (the FPI string is treated case sensitively by validators), this format (a case-insensitive match of the string !DOCTYPE HTML) is the same as found in the syntax of the SGML based HTML 4.01 DOCTYPE. Both in HTML4 and in HTML5, the formal syntax is defined in upper case letters, even if both lower case and mixes of lower case upper case are also treated as valid.
In XHTML5 the DOCTYPE must be a case-sensitive match of the string "<!DOCTYPE html>". This is because in XHTML syntax all HTML element names are required to be in lower case, including the root element referenced inside the HTML5 DOCTYPE. 
The DOCTYPE is optional in XHTML5 and may simply be omitted. However, if the markup is to be processed as both XML and HTML, a DOCTYPE should be used.


== See also ==
Document type definition contains an example
RDFa
XML schema


== References ==


== External links ==

HTML Doctype overview
Recommended DTDs to use in your Web document - an informative (not normative) W3C Quality Assurance publication
DOCTYPE grid - another overview table [Last modified 27 November 2006]
Quirks mode and transitional mode
Box model tweaking
