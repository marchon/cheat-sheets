# Top-level domain

Cloned from https://en.wikipedia.org/wiki/Top-level_domain.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 31115.

A top-level domain (TLD) is one of the domains at the highest level in the hierarchical Domain Name System of the Internet after the root domain. The top-level domain names are installed in the root zone of the name space. For all domains in lower levels, it is the last part of the domain name, that is, the last non-empty label of a fully qualified domain name. For example, in the domain name www.example.com, the top-level domain is .com. Responsibility for management of most top-level domains is delegated to specific organizations by the ICANN, an Internet multi-stakeholder community, which operates the Internet Assigned Numbers Authority (IANA), and is in charge of maintaining the DNS root zone.


== History ==
The development of top-level domains followed the introduction of the Domain Name System as a replacement for the earlier flat host-name system, in which host names and addresses were maintained in a central HOSTS.TXT file. The DNS introduced a distributed, hierarchical name space, with the unnamed root above a set of top-level domains.
Originally, the top-level domain space was organized into three main groups: Countries, Categories, and Multiorganizations. An additional temporary group consisted of only the initial DNS domain, .arpa, and was intended for transitional purposes toward the stabilization of the domain name system. In this early structure, the category domains were .gov, .edu, .com, .mil, and .org, while country domains used two-letter codes derived from ISO 3166. The multiorganization class was reserved for large organizations, especially international organizations, that did not fit easily into the other categories.
The .arpa domain was originally intended for existing ARPA-Internet hosts and was expected to be phased out once hosts moved into other domains. It was later retained and repurposed as an infrastructure top-level domain for technical uses, including reverse DNS mapping.
By 1994, RFC 1591 described the top-level domain structure as consisting of generic top-level domains and two-letter country code top-level domains. The generic domains listed at that time were .com, .edu, .net, .org, .gov, .mil, and .int. The same document described IANA as the overall authority for coordination and management of the DNS, with day-to-day registration responsibilities handled by the InterNIC and regional registries.
The number of generic top-level domains remained small until the Internet Corporation for Assigned Names and Numbers (ICANN) began later expansion rounds. In 2000, ICANN launched an application round that led to the delegation of .aero, .biz, .coop, .info, .museum, .name, and .pro. A further round begun in 2003 led to additional sponsored and generic domains, including .asia, .cat, .jobs, .mobi, .tel, .travel, and .xxx.
A much larger expansion followed ICANN's New gTLD Program, which opened its first application round in 2012. The program allowed applications for many new generic top-level domains, including internationalized domain names in non-Latin scripts, and the first new gTLDs from that round were delegated to the root zone in October 2013.


== Types ==
As of 2015, IANA distinguishes the following groups of top-level domains:

Infrastructure top-level domain (ARPA): This group consists of one domain, the Address and Routing Parameter Area. It is managed by IANA on behalf of the Internet Engineering Task Force for various purposes specified in the Request for Comments publications.
Generic top-level domains (gTLD): Top-level domains with three or more characters
Generic restricted top-level domains (grTLD): These domains are managed under official ICANN-accredited registrars.
Sponsored top-level domains (sTLD): These domains are proposed and sponsored by private agencies or organizations that establish and enforce rules restricting the eligibility to use the TLD. Use is based on community theme concepts; these domains are managed under official ICANN accredited registrars.
country-code top-level domains (ccTLD): Two-letter domains established for countries or territories. With some historical exceptions, the code for any territory is the same as its two-letter ISO 3166 code.
Internationalized country code top-level domains (IDN ccTLD): ccTLDs in non-Latin character sets (e.g., Arabic, Cyrillic, Greek, Hebrew, or Chinese).
Test top-level domains: These domains were installed under .test for testing purposes in the IDN development process; these domains are not present in the root zone.
Countries are designated in the Domain Name System by their two-letter ISO country code; there are exceptions, however (e.g., .uk). This group of domains is, therefore, commonly known as country-code top-level domains (ccTLD). Since 2009, countries with non–Latin-based scripts may apply for internationalized country code top-level domain names, which are displayed in end-user applications in their language-native script or alphabet, but use a Punycode-translated ASCII domain name in the Domain Name System.
Generic top-level domains (formerly categories) initially consisted of .gov, .edu, .com, .mil, .org, and .net. More generic TLDs have been added, such as .info.
The authoritative list of current TLDs in the root zone is published at the IANA website at https://www.iana.org/domains/root/db/ as well as tlds-alpha-by-domain.txt.


== Internationalized country code TLDs ==
An internationalized country code top-level domain (IDN ccTLD) is a top-level domain with a specially encoded domain name that is displayed in an end-user application, such as a web browser, in its language-native script or alphabet (such as the Arabic alphabet), or a non-alphabetic writing system (such as Chinese characters). IDN ccTLDs are an application of the internationalized domain name (IDN) system to top-level Internet domains assigned to countries, or independent geographic regions.
ICANN started to accept applications for IDN ccTLDs in November 2009, and installed the first set into the Domain Names System in May 2010. The first set was a group of Arabic names for the countries of Egypt, Saudi Arabia, and the United Arab Emirates. By May 2010, 21 countries had submitted applications to ICANN, representing 11 scripts.


== Infrastructure domain ==
The domain .arpa was the first Internet top-level domain. It was intended to be used only temporarily, aiding in the transition of traditional ARPANET host names to the domain name system. However, after it had been used for reverse DNS lookup, it was found impractical to retire it, and is used today exclusively for Internet infrastructure purposes such as in-addr.arpa for IPv4 and ip6.arpa for IPv6 reverse DNS resolution, uri.arpa and urn.arpa for the Dynamic Delegation Discovery System, and e164.arpa for telephone number mapping based on NAPTR DNS records. For historical reasons, .arpa is sometimes considered to be a generic top-level domain.


== Reserved domains ==
A set of domain names is reserved by the Internet Engineering Task Force as special-use domain names. The practice originated in RFC 1597 for reserved address allocations in 1994 and reserved top-level domains in RFC 2606 of 1999, with additional reservations in later RFCs. These reserved names should not be used in production networks that utilize the global domain name system.


== Historical domains ==

In the late 1980s, InterNIC created the .nato domain for use by NATO. NATO considered none of the then-existing TLDs as adequately reflecting their status as an international organization. Soon after this addition, however, InterNIC also created the .int TLD for the use by international organizations in general, and persuaded NATO to use the second level domain nato.int instead. The nato TLD, no longer used, was finally removed in July 1996.
Other historical TLDs are .cs for Czechoslovakia (now using .cz for Czech Republic and .sk for Slovakia), .dd for East Germany (using .de after reunification of Germany), .yu for SFR Yugoslavia and Serbia and Montenegro (now using .ba for Bosnia and Herzegovina, .hr for Croatia, .me for Montenegro, .mk for North Macedonia, .rs for Serbia and .si for Slovenia), .zr for Zaire (now .cd for the Democratic Republic of the Congo), and .an for Netherlands Antilles (now .aw for Aruba, .cw for Curaçao and .sx for Sint Maarten). In contrast to these, the TLD .su has remained active despite the collapse of the Soviet Union that it represents. Under the chairmanship of Nigel Roberts, ICANN's ccNSO is working on a policy for the retirement of ccTLDs that have been removed from ISO 3166.


== Proposed domains ==

Around late 2000, ICANN discussed and finally introduced .aero, .biz, .coop, .info, .museum, .name, and .pro TLDs. Site owners argued that a similar TLD should be made available for adult and pornographic websites to settle the dispute of obscene content on the Internet, to address the responsibility of US service providers under the US Communications Decency Act of 1996. Several options were proposed including xxx, sex and adult. The .xxx top-level domain eventually went live in 2011.
An older proposal consisted of seven new gTLDs: arts, firm, .info, nom, rec, .shop, and .web. Later .biz, .info, .museum, and .name covered most of these old proposals.
During the 32nd International Public ICANN Meeting in Paris in 2008, ICANN started a new process of TLD naming policy to take a "significant step forward on the introduction of new generic top-level domains". This program envisioned the availability of many new or already proposed domains, as well as a new application and implementation process. Observers believed that the new rules could result in hundreds of new gTLDs being registered.
On 13 June 2012, ICANN announced nearly 2,000 applications for top-level domains, which began installation throughout 2013. The first seven – bike, clothing, guru, holdings, plumbing, singles, and ventures – were released in 2014. As of 2025, there are approximately 1,200 delegated generic top-level domains (gTLDs) in the global Domain Name System, including legacy gTLDs (such as .com, .org, .net) and gTLDs introduced in the 2012 New gTLD Program. 
ICANN has been gearing to roll out the subsequent round of New gTLD expansion but opening the second round of New gTLD Application window in April 2026 for 12 – 15 weeks. The first draft of New gTLD Applicant Guidebook was published on 30 May 2025 followed by the period of public comments has now been approved by the ICANN board and is now expected to be published in ICANN's website by December 2025.
ICANN has also opened up Applicant Support Program to support organizations and communities which are in need of financial support to apply for New gTLD. The application window to apply for financial support has been extended until 19 December 2025 from the original deadline of 19 November 2025. ICANN has also mandated applicants to choose a registry backend service provider from ICANN's accredited Registry Service Provider (RSP) list which is expected to be published in early 2026. ICANN is publishing timely updates on their website.  


=== Rejected domains ===
ICANN rejected several proposed domains to include .home and .corp due to conflicts regarding gTLDs that are in use in internal networks.
Investigation into the conflicts was conducted at ICANN's request by Interisle Consulting. The resulting report was to become known as the Name Collision issue, which was first reported at ICANN 47.


== Dotless domains ==

Due to the structure of DNS, each node in the tree has its own collection of records, and since top-level domains are nodes in DNS, they have records of their own. For example, querying org itself (with a tool such as dig, host, or nslookup) returns information on its nameservers:

Dotless domains are top-level domains that take advantage of that fact, and implement A, AAAA or MX DNS records to serve webpages or allow incoming email directly on a TLD – for example, a webpage hosted on http://example/, or an email address user@example.
ICANN and IAB have spoken out against the practice, classifying it as a security risk among other concerns. ICANN's Security and Stability Advisory Committee (SSAC) additionally claims that SMTP "requires at least two labels in the FQDN of a mail address" and, as such, mail servers would reject emails to addresses with dotless domains.
ICANN has also published a resolution in 2013 that prohibits the creation of dotless domains on gTLDs. ccTLDs, however, fall largely under their respective country's jurisdiction, and not under ICANN's. Because of this, there have been many examples of dotless domains on ccTLDs in spite of ICANN's vocal opposition.
As of July 2025, that is the case of:

Uzbekistan's .uz, online at https://uz./ (Deprecated link archived 4 September 2023 at archive.today)It is a mirror of https://cctld.uz/, albeit with an invalid certificate.
In 2023, it used to be the case of:

Anguilla's .ai, online at http://ai./ (Deprecated link archived 22 January 2023 at archive.today)It simply displayed a notice that the website was no longer public.The TLD no longer has an A or AAAA record.
Other ccTLDs with A or AAAA records, as of July 2025, include: .cm, .tk and .ws.
A similar query to org's presented above could be made for ai, which showed A and MX records for the TLD:

Historically, many other ccTLDs have had A or AAAA records. On 3 September 2013, as reported by the IETF, they were the following: .ac, .dk, .gg, .io, .je, .kh, .sh, .tm, .to, and .vi.


=== New TLDs ===
Following a 2014 resolution by ICANN, newly registered TLDs must implement the following A, MX, TXT, and SRV apex DNS records – where <TLD> stands for the registered TLD – for at least 90 days:

This requirement is meant to avoid domain name collisions when new TLDs are registered. For example, programmers may have used custom local domains such as foo.bar or test.dev, which would both collide with the creation of gTLDs .bar in 2014 and .dev in 2019.
While this does create apex DNS records of type A and MX, they do not qualify as a dotless domain, as the records should not point to real servers. For instance, the A record contains the IP 127.0.53.53, a loopback address (see IPv4 § Addressing), picked as a mnemonic to indicate a DNS-related problem, as DNS uses port 53.


== Pseudo-domains ==

Several networks, such as BITNET, CSNET, and UUCP, existed that were in widespread use among computer professionals and academic users, but were not interoperable directly with the Internet and exchanged mail with the Internet via special email gateways. For relaying purposes on the gateways, messages associated with these networks were labeled with suffixes such as .bitnet, .oz, .csnet, or .uucp, but these domains did not exist as top-level domains in the public Domain Name System of the Internet.
Most of these networks have long since ceased to exist, and although UUCP still gets significant use in parts of the world where Internet infrastructure has not yet become well established, it subsequently transitioned to using Internet domain names, and pseudo-domains now largely survive as historical relics. One notable exception is the 2007 emergence of SWIFTNet Mail, which uses the swift pseudo-domain.
The anonymity network Tor formerly used the top-level pseudo-domain .onion for onion services, which can only be reached with a Tor client because it uses the Tor onion routing protocol to reach the hidden service to protect the anonymity of users. However, the pseudo-domain became officially reserved in October 2015. i2p provides a similar hidden pseudo-domain, .i2p, and Namecoin uses the .bit pseudo-domain.


== Examples ==


== See also ==
Alternative DNS root
Domain hack
Domain name registrar
List of Internet top-level domains
Public Suffix List
Second-level domain


== Notes ==


== References ==


== Further reading ==
Addressing the World: National Identity and Internet Country Code Domains, edited by Erica Schlesinger Wass (Rowman & Littlefield, 2003, ISBN 0-7425-2810-3) examines connections between cultures and their ccTLDs.
Ruling the Root by Milton Mueller (MIT Press, 2001, ISBN 0-262-13412-8) discusses TLDs and domain name policy more generally.


== External links ==

Root Zone Database – list of TLDs on the DNS Root Zone, IANA
IANA TLD List (plain text, ALL-CAPS)
New TLDs – Articles on CircleID about TLDs
"Top-Level Domain Names by Host Count". ISC. January 2008. Retrieved 7 August 2008.
TLDs accepted in 2012 (archived)
