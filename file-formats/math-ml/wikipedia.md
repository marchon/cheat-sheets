# MathML

Cloned from https://en.wikipedia.org/wiki/MathML.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 52313.

Mathematical Markup Language (MathML) is a pair of mathematical markup languages, an application of XML for describing mathematical notation and capturing both its structure and content. Its aim is to natively integrate mathematical formulae into World Wide Web pages and other documents. It is part of HTML5 and standardised by ISO/IEC since 2015.


== History ==
Following some experiments in the Arena browser based on proposals for mathematical markup in HTML, MathML 1 was released as a W3C recommendation in April 1998 as the first XML language to be recommended by the W3C. Version 1.01 of the format was released in July 1999 and version 2.0 appeared in February 2001. Implementations of the specification appeared in Amaya 1.1, Mozilla 1.0 and Opera 9.5. In October 2003, the second edition of MathML Version 2.0 was published as the final release by the W3C Math Working Group.
MathML was originally designed before the finalization of XML namespaces. However, it was assigned a namespace immediately after the Namespace Recommendation was completed, and for XML use, the elements should be in the namespace with namespace URL http://www.w3.org/1998/Math/MathML. When MathML is used in HTML (as opposed to XML) this namespace is automatically inferred by the HTML parser and need not be specified in the document.


=== MathML version 3 ===
Version 3 of the MathML specification was released as a W3C recommendation on 20 October 2010. A recommendation of A MathML for CSS Profile was later released on 7 June 2011; this is a subset of MathML suitable for CSS formatting. Another subset, Strict Content MathML, provides a subset of content MathML with a uniform structure and is designed to be compatible with OpenMath. Other content elements are defined in terms of a transformation to the strict subset. New content elements include <bind> which associates bound variables (<bvar>) to expressions, for example a summation index. The new <share> element allows structure sharing.
The development of MathML 3.0 went through a number of stages. In June 2006, the W3C rechartered the MathML Working Group to produce a MathML 3 Recommendation until February 2008, and in November 2008 extended the charter to April 2010. A sixth Working Draft of the MathML 3 revision was published in June 2009. On 10 August 2010 version 3 graduated to become a "Proposed Recommendation" rather than a draft. An implementation of MathML 2 landed in WebKit around this same time, with a Chromium implementation following a couple of years later, although that implementation was removed from Chromium after less than a year.
The Second Edition of MathML 3.0 was published as a W3C Recommendation on 10 April 2014. The specification was approved as an ISO/IEC international standard 40314:2015 on 23 June 2015. Also in 2015, the MathML Association was founded to support the adoption of the MathML standard. At that time, according to a member of the MathJax team, none of the major browser makers paid any of their developers for any MathML-rendering work; whatever support existed was overwhelmingly the result of unpaid volunteer time/work.


=== MathML Core ===
In August 2021, a new specification called MathML Core was published, described as the "core subset of Mathematical Markup Language, or MathML, that is suitable for browser implementation." MathML Core set itself apart from MathML 3.0 by including detailed rendering rules and integration with CSS, automated browser support testing resources, and focusing on a fundamental subset of MathML. An implementation was added to Chromium at the beginning of 2023.


== Presentation and semantics ==

MathML deals not only with the presentation but also the meaning of formula components (the latter part of MathML is known as "Content MathML"). Because the meaning of the equation is preserved separate from the presentation, how the content is communicated can be left up to the user. For example, web pages with MathML embedded in them can be viewed as normal web pages with many browsers, but visually impaired users can also have the same MathML read to them through the use of screen readers (e.g. using the VoiceOver in Safari). JAWS from version 16 onward supports MathML voicing as well as braille output.
The quality of rendering of MathML in a browser depends on the installed fonts. The STIX Fonts project have released a comprehensive set of mathematical fonts under an open license. The Cambria Math font supplied with Microsoft Windows had slightly more limited support.
A valid MathML document typically consists of the XML declaration, DOCTYPE declaration, and document element. The document body then contains MathML expressions which appear in <math> elements as needed in the document. Often, MathML will be embedded in more general documents, such as HTML, DocBook, or other XML-based formats.


=== Presentation MathML ===

Presentation MathML focuses on the display of an equation, and has about 30 elements. The elements' names all begin with m. A Presentation MathML expression is built up out of tokens that are combined using higher-level elements, which control their layout. Finer details of presentation are affected by close to 50 attributes.
Token elements generally only contain characters (not other elements). They include:

<mi>x</mi> – identifiers;
<mo>+</mo> – operators;
<mn>2</mn> – numbers;
<mtext>such that</mtext> – text.
Note, however, that these token elements may be used as extension points, allowing markup in host languages.
MathML in HTML5 allows most inline HTML markup in mtext, and <mtext><b>non</b> zero</mtext> is conforming, with the HTML markup being used within the MathML to mark up the embedded text (making the first word bold in this example).
These are combined using layout elements, that generally contain only elements. They include:

<mrow> – a horizontal row of items;
<msup>, <munderover>, and others – superscripts, limits over and under operators like sums, etc.;
<mfrac> – fractions;
<msqrt> and <mroot> – roots;
<mfenced> – surrounding content with fences, such as parentheses.
As usual in HTML and XML, many entities are available for specifying special symbols by name, such as &pi; and &RightArrow;. An interesting feature of MathML is that entities also exist to express normally-invisible operators, such as &InvisibleTimes; (or the shorthand &it;) for implicit multiplication. They are:

U+2061  FUNCTION APPLICATION (to distinguish 
  
    
      
        sin
        ⁡
        (
        x
        )
      
    
    {\displaystyle \sin(x)}
  
 from 
  
    
      
        
          sin
        
        ⋅
        x
      
    
    {\displaystyle {\sin }\cdot x}
  
 in 
  
    
      
        sin
        ⁡
        
          x
        
      
    
    {\displaystyle \sin {x}}
  
);
U+2062  INVISIBLE TIMES (to distinguish 
  
    
      
        
          a
          
            m
            ×
            n
          
        
      
    
    {\displaystyle a_{m\times n}}
  
 from 
  
    
      
        
          a
          
            m
            ,
            n
          
        
      
    
    {\displaystyle a_{m,n}}
  
 in 
  
    
      
        
          a
          
            m
            n
          
        
      
    
    {\displaystyle a_{mn}}
  
);
U+2063  INVISIBLE SEPARATOR (vice versa);
U+2064  INVISIBLE PLUS (to distinguish 
  
    
      
        2
        +
        
          
            1
            3
          
        
      
    
    {\displaystyle 2+{\frac {1}{3}}}
  
 from 
  
    
      
        2
        ⋅
        
          
            1
            3
          
        
      
    
    {\displaystyle 2\cdot {\frac {1}{3}}}
  
 in 
  
    
      
        2
        
          
            
              1
              3
            
          
        
      
    
    {\displaystyle 2{\tfrac {1}{3}}}
  
).
The full specification of MathML entities is closely coordinated with the corresponding specifications for use with HTML and XML in general.
Thus, the expression 
  
    
      
        a
        
          x
          
            2
          
        
        +
        b
        x
        +
        c
      
    
    {\displaystyle ax^{2}+bx+c}
  
 requires two layout elements: one to create the overall horizontal row and one for the superscripted exponent. However, the individual tokens also have to be identified as identifiers (<mi>), operators (<mo>), or numbers (<mn>). Adding the token markup, the full form ends up as

A complete document that consists of just the MathML example above, is shown here:


=== Content MathML ===

Content MathML focuses on the semantics, or meaning, of the expression rather than its layout. Central to Content MathML is the <apply> element that represents function application. The function being applied is the first child element under <apply>, and its operands or parameters are the remaining child elements. Content MathML uses only a few attributes.
Tokens such as identifiers and numbers are individually marked up, much as for Presentation MathML, but with elements such as <ci> and <cn>. Rather than being merely another type of token, operators are represented by specific elements, whose mathematical semantics are known to MathML: <times>, <power>, etc. There are over a hundred different elements for different functions and operators.
For example, <apply><sin/><ci>x</ci></apply> represents 
  
    
      
        sin
        ⁡
        (
        x
        )
      
    
    {\displaystyle \sin(x)}
  
 and <apply><plus/><ci>x</ci><cn>5</cn></apply> represents 
  
    
      
        x
        +
        5
      
    
    {\displaystyle x+5}
  
. The elements representing operators and functions are empty elements, because their operands are the other elements under the containing <apply>.
The expression 
  
    
      
        a
        
          x
          
            2
          
        
        +
        b
        x
        +
        c
      
    
    {\displaystyle ax^{2}+bx+c}
  
 could be represented as

Content MathML is nearly isomorphic to expressions in a functional language such as Scheme and other dialects of Lisp. <apply>...</apply> amounts to Scheme's (...), and the many operator and function elements amount to Scheme functions. With this trivial literal transformation, plus un-tagging the individual tokens, the example above becomes:

This reflects the long-known close relationship between XML element structures, and LISP or Scheme S-expressions.


==== Wikidata annotation in Content MathML ====
According to the OM Society, OpenMath Content Dictionaries can be employed as collections of symbols and identifiers with declarations of their semantics – names, descriptions and rules. A 2018 paper presented at the SIGIR conference proposed that the semantic knowledge base Wikidata could be used as an OpenMath Content Dictionary to link semantic elements of a mathematical formula to unique and language-independent Wikidata items.


== Example ==
The well-known quadratic formula could be represented in Presentation MathML as an expression tree made up from layout elements like <mfrac> or <msqrt>:

This example uses the <annotation> element, which can be used to embed a semantic annotation in non-XML format, for example to store the formula in the format used by an equation editor such as StarMath or the markup using LaTeX syntax. The encoding field is usually a MIME type, although most of the equation encodings don't have such a registration; freeform text may be used in such cases.
Although less compact than other formats, the XML structuring of MathML makes its content widely usable and accessible, allows near-instant display in applications such as web browsers, and facilitates an interpretation of its meaning in mathematical software products. MathML is not intended to be written or edited directly by humans.


== Embedding MathML in HTML/XHTML files ==
MathML, being XML, can be embedded inside other XML files such as XHTML files using XML namespaces.

Inline MathML is also supported in HTML5 files. There is no need to specify namespaces as there was in XHTML.


== Embedding MathML in OpenDocument Office Suite files ==
MathML is natively supported within the ISO standardised OpenDocument Format, which is the default office suite file format used in LibreOffice, Collabora Online and others, these have the filename extensions .odt, .ods, and .odp. The specific XML element <math:math> serves as a container for the MathML content, ensuring it is correctly interpreted within the OpenDocument framework.
Microsoft Office does not support MathML natively within its default proprietary XML file formats (.docx, .xlsx, .pptx): instead, it defines a different XML math syntax derived from older Microsoft Office products. When Microsoft Office saves equations in the OpenDocument Format, it may save equations as uneditable images, losing the ability for the equation to be edited in the future and causing loss of information. This is a Microsoft Office issue, workarounds exist, including: Updating Word, ensuring equations are in the latest format, disabling AutoSave and using the "Save as MathML" option.


== Other standards ==
Another standard called OpenMath that has been more specifically designed (largely by the same people who devised Content MathML) for storing formulae semantically can be used to complement MathML. OpenMath data can be embedded in MathML using the <annotation-xml encoding="OpenMath"> element. OpenMath content dictionaries can be used to define the meaning of <csymbol> elements. The following would define P1(x) to be the first Legendre polynomial:

OpenMath support is part of the OpenDocument office suite specification, which explicitly allows embedding OpenMath objects alongside MathML. Such that MathML renders the equation and an OpenMath is a semantic representation so that software can compute with it. Office suites that default to using the OpenDocument standard, such as LibreOffice and Collabora Online currently stick to the MathML standard for interoperability, comparatively, OpenMath is not defined in Microsoft's proprietary document formats for docx, pptx, and xlsx.
The OMDoc format has been created for markup of larger mathematical structures than formulae, from statements like definitions, theorems, proofs, and examples, to complete theories and even entire text books. Formulae in OMDoc documents can either be written in Content MathML or in OpenMath; for presentation, they are converted to Presentation MathML.


== See also ==

CSS
List of document markup languages
Comparison of document markup languages
Formula editors
LaTeX2HTML
LaTeXML
KaTeX – JavaScript library that converts LaTeX to MathML
MathJax – JavaScript library that converts LaTeX to MathML
OpenDocument The ISO/IEC standard used by applications like LibreOffice and Collabora Online natively support MathML for mathematical content


== References ==


== Further reading ==


=== Specifications ===
W3C Recommendation: Mathematical Markup Language (MathML) 1.01 Specification
W3C Recommendation: Mathematical Markup Language (MathML) Version 2.0 (Second Edition)
W3C Recommendation: Mathematical Markup Language (MathML) Version 3.0 (Third Edition)


== External links ==
W3C Math Home – Contains the specifications, a FAQ, and a list of supporting software.
Pavi, Sandhu (12 December 2002). "The MathML Handbook". Charles River Media. Retrieved 2 October 2015.
web-xslt  – A collection of XSLT programs for handling MathML (e.g. converting Content MathML to Presentation MathML, converting Presentation MathML to TeX)
