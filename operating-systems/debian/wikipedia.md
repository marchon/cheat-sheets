# Debian

Cloned from https://en.wikipedia.org/wiki/Debian.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 8242.

Debian () is a free, general-purpose operating system developed by the Debian Project, a worldwide volunteer association founded by Ian Murdock on August 16, 1993. It is the second-oldest Linux distribution still being developed (only Slackware is older) and forms the base of many others.
It is deployed across servers, personal computers, and embedded devices. Among Linux distributions, it ranks second only to Ubuntu (a Debian derivative), with 16% of the overall market. According to the 2025 Stack Overflow Developer Survey, 11.4% of developers use it as their primary personal operating system and 10.4% professionally. Its emphasis on stability and long-term support over frequent package updates has made it prevalent in server and embedded deployments.
Development is led by the Project Leader and guided by two foundational documents: the Debian Social Contract, a summary of the project's commitments that includes the Debian Free Software Guidelines (DFSG), and the Debian Constitution, which describes the organizational structure. The project publishes three concurrent development branches: stable, testing, and unstable, which correspond to different levels of software maturity. The current stable release, released on August 9, 2025 and codenamed "Trixie", includes tens of thousands of packages maintained by more than a thousand active contributors.
Since 1997, the project has operated independently through Software in the Public Interest, a non-profit corporation founded by project members to hold its assets and trademarks. It previously received support from the Free Software Foundation between 1994 and 1995, with the sponsorship ending due to disagreements.


== History ==


=== Version history ===

Debian uses version numbers and code names based on the characters of the Toy Story franchise to refer to its releases. This naming convention was introduced by former project leader Bruce Perens, who was working at Pixar at the time. The unstable branch is permanently named after Sid, the neighborhood child known for destroying toys.


=== Founding (1993–1999) ===


==== Debian Linux Manifesto (1993) ====

The first public mention of the project occurred on August 16, 1993, when Ian Murdock posted an announcement to the comp.os.linux.development newsgroup. Murdock founded the project due to his dissatisfaction with the Softlanding Linux System; after making extensive modifications to this system, he concluded that it would be more efficient to develop a new distribution from scratch. Similar to the original announcement of Linux, Murdock's post solicited feedback and suggestions on how the system could be improved. The name Debian was a portmanteau of his first name and that of his then-wife, Deborah Lynn.
The first internal release, pre-alpha 0.01, came out on September 15, 1993. The first public versions, beta 0.90 and beta 0.91, followed on January 26 and 29, 1994, respectively, with their mailing lists hosted by Pixar. These releases included the Debian Linux Manifesto, in which Murdock outlined his vision for the project, advocating for a distribution "developed openly in the spirit of Linux and GNU".


==== Free Software Foundation sponsorship (1994–1995) ====
Between November 1994 and November 1995, the project was sponsored by the Free Software Foundation (FSF), whose sponsorship Murdock sought with the hope that it would also give the FSF experience in packaging a complete GNU system. In March 1995, Murdock stepped down as project leader to dedicate more time to his studies, work, and family; the new team did not seek to continue the sponsorship. While the Debian Project remained aligned with the FSF's political and philosophical goals, differences in technical direction ended the arrangement, with the FSF invited to continue participating in the project on the same basis as individual developers and other contributing organizations.


==== Bruce Perens as project leader (1996–1997) ====

In April 1996, Bruce Perens became the project leader. On June 17 of the same year, Debian 1.1 "Buzz" was released, the first release under his leadership. By that time, Ian Jackson's dpkg had already become an integral part of Debian. The concept of a social contract with the free software community was suggested to Perens by Ean Schussler; Perens composed a draft, which was subsequently refined by Debian developers through email discussion over most of June and approved by vote, producing the Debian Social Contract and the DFSG, published on July 4, 1997. He created BusyBox to enable running the installer from a single floppy disk. By the time Debian 1.2 "Rex" was released on December 12, 1996, the project had grown to nearly 200 volunteers. Perens stepped down as project leader in December 1997 and left the project entirely on March 18, 1998.


==== Formation of Software in the Public Interest (1997) ====
On June 16, 1997, following the end of the FSF sponsorship, Debian motivated the formation of Software in the Public Interest (SPI), a non-profit corporation registered in the state of New York. SPI was founded to help Debian and other similar organizations develop and distribute open hardware and software, acting as a fiscal sponsor by handling non-technical administrative tasks so that projects are not required to operate their own legal entity.


==== Ian Jackson and Wichert Akkerman leadership (1998–1999) ====
Ian Jackson became project leader in January 1998. Debian 2.0 "Hamm", released on July 24, 1998, was the first multi-architecture release of Debian, adding support for the Motorola 68000 family. On December 2, 1998, the Debian Constitution was ratified for the first time, simultaneously initiating the election process that would result in Wichert Akkerman succeeding Jackson as project leader in January 1999. On March 9, 1999, Debian 2.1 "Slink" was released, alongside the package manager front-end APT. On May 23, 1999, the Internal Revenue Service determined that SPI qualifies for 501(c)(3) status, allowing the Debian Project to accept tax deductible contributions in the United States.


=== Consolidation (2000–2004) ===


==== Package pools and the testing branch (2000) ====
On December 13, 2000, Debian activated package pools on its ftp-master archive server, allowing the "Woody" release to be prepared. A package pool is a collection of a package's versions, which Debian's branches draw from for their packages. This change enabled special-purpose distributions, including a new testing branch that was used to prepare "Woody" for release. Under this system, packages in the unstable branch considered to be sufficiently reliable were promoted to testing after a waiting period of several weeks, a mechanism intended to reduce freeze time and allow the project to prepare a new release at any point.


==== First DebConf (2000) ====
The first Debian Conference was held in Bordeaux, France, from July 5 to 9, 2000. The event brought Debian developers and advanced users together in person for the first time, giving the Debian project a physical presence rather than existing solely as an online collective. In addition to working sessions, the conference served as a venue for attendees to meet other members of the free software community, with some presentations open to the general public. Discussion topics included the Debian user base and its adoption in corporate settings and derived distributions, ongoing development of "Woody", the Debian GNU/Hurd port, the project's quality-control processes, the procedure for becoming a Debian developer, and tools such as debconf and boot-floppies. The program combined presentations, technical talks, birds-of-a-feather sessions, and coding parties.


==== HP's adoption of Debian (2001) ====
In May 2001, Hewlett-Packard (HP) announced that it would use Debian for its future Linux development work. Martin Fink, HP's general manager of Linux systems operations, said the company chose Debian because it was the most free and open Linux distribution available, a factor he believed would help prevent proprietary software from dominating efforts to establish a standardized Linux platform, since Debian was not controlled by a single commercial entity. Debian developer Bruce Perens, who acted as HP's Linux advocate, disclosed the decision in an email to the Debian development mailing list, noting that HP had already begun distributing Debian to customers and planned to offer support and training for it. Perens described the move as an initial step toward HP's broader support for the Linux Standard Base project.


==== Debian "Woody" release (2002) ====

Debian 3 "Woody" was released on July 19, 2002, expanding the project's scope. Supported by a community of over 900 developers and led by newly appointed Project Leader Bdale Garbee, the release included approximately 8,500 binary packages distributed across seven official binary CDs. This version broadened hardware compatibility by introducing support for several new architectures, including IA-64, HP PA-RISC, MIPS (both big and little endian), and S/390. It was the first Debian release to incorporate cryptographic software, following the relaxation of Cold War US cryptography export restrictions, as well as the first to feature the KDE desktop environment after its Qt licensing issues were resolved.


==== University of Twente server fire (2002) ====
On November 20, 2002, a fire destroyed the network operations center at the University of Twente in the Netherlands, which hosted one of Debian's servers, satie.debian.org. The blaze broke out around 8:00 a.m. local time and consumed the building so thoroughly that firefighters could not save the server room. Because satie had hosted the project's security archive, its non-US archive, and the databases supporting new-maintainer applications and quality assurance, the corresponding services (security.debian.org, non-us.debian.org, nm.debian.org, and qa.debian.org) went offline as a result. Debian subsequently rebuilt these services on another host, klecker, which had recently been relocated from the United States to the Netherlands.


==== Ubuntu fork and the compatibility debate (2004) ====
On October 20, 2004, Mark Shuttleworth announced the first release of Ubuntu, a new Debian-derived distribution aimed at combining Debian's extensive package base with a faster installer, a fixed six-month release cycle, and 18 months of security support per release, under the version 4.10 and the codename "Warty Warthog". The rapid growth of Ubuntu sparked debate within the Debian community regarding the long-term compatibility of Debian-derived distributions. Some Debian developers warned that as more developers began building packages targeting Ubuntu rather than Debian proper, divergence between the two could erode that compatibility, mimicking the fragmentation seen among RPM-based distributions. Other community members argued that Debian should address its lengthy release cycles, calling for a predictable, time-based release schedule similar to that adopted by the GNOME Project, in order to reduce the incentive for downstream distributions to fork.


=== Maturity and controversies (2005–2015) ===


==== Debian 3.1 "Sarge" release (2005) ====

Debian 3.1 "Sarge" was released on 6 June 2005, shortly after Branden Robinson had been appointed Project Leader. Sarge was the first release to include a complete office suite, OpenOffice.org 1.1, and the first stable release to use the Debian-Installer, replacing the older boot-floppies method. The new installer featured a modular design intended to support future extensibility and had been fully translated into almost forty languages. Additional features included improved hardware detection, support for booting from USB flash drives, use of aptitude for package installation during base system configuration, and support for the XFS file system, RAID, and LVM.


==== Debian–Mozilla trademark dispute (2006) ====

In 2006, following a debate that began in 2004, Mozilla's software was renamed in Debian for two reasons: the Firefox logo was under a proprietary license incompatible with the DFSG, and a Mozilla Corporation representative stated that programs with unapproved modifications could not be distributed under its trademarks. Because Debian applied security patches without prior approval from Mozilla, a practice consistent with its package maintenance policy, the project began distributing the browser Firefox as Iceweasel, the email client Thunderbird as Icedove, and the Internet suite SeaMonkey as Iceape. The renamings were implemented in the unstable branch in 2006 and reached the stable release with the launch of Debian 4.0 "Etch" in 2007.


==== Dunc-Tank funding controversy (2006) ====

Debian 4.0 "Etch" was released on April 8, 2007, following a delay caused by a protest by unpaid developers. The protest started in 2006 after two release managers accepted payment from Dunc-Tank, an organization composed entirely of project members, to accelerate Etch's release. In response, some developers deliberately reduced their contributions to the project. Critics argued that the project had traditionally relied on voluntary work, and that introducing paid contributors created an inconsistency in which only two of roughly 1,000 developers would be compensated. Some also contended that if funding were to be introduced, it should be extended to all developers, since their contributions were considered equally important to those of the release managers.


==== OpenSSL predictable key vulnerability (2008) ====
On May 13, 2008, Debian developer Luciano Bello discovered that the OpenSSL library distributed with Debian and derivatives such as Ubuntu generated security keys that were vulnerable to a brute-force attack. Only 32,767 different keys were produced, making the cryptographic key material easily guessable. The weakness was caused by changes made in May 2006 by another Debian developer in response to warnings from the memory debugging tool Valgrind, which indicated that OpenSSL was using memory that had not been initialized to a known state. Normally, using uninitialized memory in this way would be considered a programming error. In this case, however, the OpenSSL library was intentionally relying on that uninitialized memory as a source of randomness. As a result, removing the supposed error also removed the randomness the software depended on for key generation. Many key types were affected, including SSH, OpenVPN, and DNSSEC keys, as well as key material used in X.509 certificates and SSL/TLS sessions. Resolving the issue was not simple, since patching the vulnerability alone was insufficient; all affected keys and certificates also had to be regenerated.


==== Time-based release cycle and official backports (2009-2010) ====
On July 29, 2009, Debian adopted a policy of time based development freezes on a two year cycle, under which freezes would occur in December of every odd numbered year, with releases following sometime in the first half of every even numbered year. This change was intended to provide better predictability of releases for users, allow developers to do better long term planning, give more time for disruptive changes so as to reduce inconvenience for users, and reduce overall freeze time.
On September 5, 2010, the Debian backports service became official. Backports are packages from the testing branch recompiled for the current stable or oldstable release, allowing users to install more recent versions of programs without sacrificing the overall stability of the system. The original service was created by Debian developer Norbert Tretkowski with support from team(ix), and was later further developed with the help of Debian developers Alexander Wirt and Jörg Jaspert.


==== Debian "Squeeze" release (2011) ====
Debian 6 "Squeeze", released on 6 February 2011, was the first version whose Linux kernel was distributed entirely without proprietary firmware, with non-free components moved to a separate repository, allowing users to install them if needed. It was also the first release to come with two "flavors", Debian GNU/Linux and Debian GNU/kFreeBSD, the latter introduced as a technology preview.


==== Systemd adoption debate (2014) ====

Between 2013 and 2014, the Debian Technical Committee deliberated on the choice of default init system for the next stable release, evaluating options such as systemd, Upstart, and OpenRC. The decision, made in February 2014 in favor of systemd, sparked debate within the community and resulted in the resignation of some developers, including Ian Jackson. Debian 8 "Jessie", released on April 25, 2015, was the first version to adopt systemd as the default.


==== Microsoft Azure endorsement (2015) ====
On December 2, 2015, the Microsoft Azure Team, in collaboration with the consulting and services company Credativ, announced Debian as an endorsed distribution on the Azure Marketplace, allowing customers to provision Debian-based virtual machines on Microsoft Azure.


==== Death of Ian Murdock (2015) ====
On December 28, 2015, Debian project founder Ian Murdock died in San Francisco, California, at the age of 42. In the days before his death, he had published a series of Twitter messages describing a conflict with the San Francisco Police Department. The cause of death was initially unknown, but on July 6, 2016, CNNMoney reported that it had obtained the autopsy record from the San Francisco medical examiner's office. According to the report, police officers had entered Murdock's home and found him dead, with a vacuum cleaner's electrical cord wound tightly around his neck. After his death, the Debian project published a memorial in which he was described as the "stalwart proponent of Free Open Source Software, Father, Son, and the 'ian' in Debian."


=== Recent history (2016–present) ===


==== Mozilla software renaming reversal (2017) ====
Starting in 2016 and completed in 2017 with Debian 9 "Stretch", Mozilla Corporation's software was renamed back to its official versions, after the company relicensed the logos under a copyright license compatible with the DFSG and acknowledged that the patches applied by Debian did not compromise the product's quality, allowing the project to return to its original visual identity.


==== Windows Subsystem for Linux availability (2018) ====
In March 2018, Debian became available for download from the Microsoft Store for installation on the Windows Subsystem for Linux (WSL). WSL allows developers to install a Linux distribution and use Linux programs on Windows without the overhead of a virtual machine or dual boot setup.


==== "Buster" and "Bullseye" releases (2019–2021) ====

Debian 10 "Buster", released on 6 July 2019, introduced advances in the areas of security and graphical infrastructure. Among the main changes were the addition of UEFI Secure Boot support, the enabling of AppArmor by default, and the adoption of Wayland as the default display server protocol for the GNOME desktop environment. In this release, the project also published a resolution that consolidated systemd as the system's init. Debian 11 "Bullseye", released on 14 August 2021, activated systemd's persistent journal functionality by default, introduced driverless scanning support via the sane-escl backend, and became the first release with kernel-level support for the exFAT filesystem, defaulting to it for mounting exFAT drives.


==== XZ Utils backdoor (2024) ====

On March 29, 2024, Microsoft developer and engineer Andres Freund discovered a backdoor in XZ Utils, a compression library, after noticing unusual CPU usage and errors generated by Valgrind, a tool for memory debugging, while troubleshooting SSH performance on Debian "Sid" (unstable). The backdoor was later traced to years of social engineering and code contributions by a contributor using the name Jia Tan. It allowed an attacker with a specific private key to hijack sshd, the executable responsible for handling SSH connections, and execute arbitrary commands. The vulnerability was assigned the identifier CVE-2024-3094 and given the maximum CVSS severity score of 10.0. The compromised code affected Debian's testing, unstable, and experimental suites, among other Linux distributions.


==== "Bookworm" and "Trixie" releases (2023–2025) ====
Debian 12 "Bookworm", released on June 10, 2023, was the first stable release to include non-free firmware packages by default in the installer when the system detects that they are necessary. This followed the 2022 General Resolution on non-free firmware, which decided to amend the Debian Social Contract to permit the inclusion of firmware that is otherwise not part of the system, in order to enable the use of Debian on hardware that requires it. Debian 13 "Trixie", released on August 9, 2025, added support for the riscv64 architecture and dropped support for i386 as a regular architecture, meaning there is no official kernel or Debian-Installer for it.


== Distribution ==

Debian provides its entire distribution free of charge. The project does not manufacture CDs, DVDs, Blu-ray discs, or USB flash drives, relying instead on third-party vendors for that purpose. To help vendors produce disks of consistent quality, Debian supplies official images that have been fully tested by its testing team.
The Debian distribution is mirrored on hundreds of servers worldwide. In addition to HTTP and FTP, images can be obtained through other download methods. Jigsaw Download, commonly known as jigdo, is a bandwidth friendly method of distributing Debian USB, CD, and DVD images. BitTorrent, a peer-to-peer download system optimised for large numbers of simultaneous downloaders, is also supported, and requires the use of a BitTorrent client. The Debian distribution itself includes such tools, among them aria2, Transmission, qBittorrent, and KTorrent, while users of other operating systems, such as Windows and macOS, can use clients including qBittorrent and BitTorrent.
Users may purchase a set of CDs, DVDs, or a USB stick from a vendor, or they may download the installation images from a Debian mirror and create their own installation media, provided they have a sufficiently fast network connection along with a CD or DVD burner or a USB flash drive. Once such installation media has been created, and assuming it is bootable on the target machine, the installation process can proceed directly to booting the installation system.


=== Image sizes ===
Debian offers its images in several sizes to accommodate different types of media. CD images are up to 700 megabytes in size and are suitable for writing to standard CD-R or CD-RW media. DVD images are up to 4.7 gigabytes in size and are suitable for writing to standard DVD-R, DVD+R, and similar media.


=== USB installation media ===
Debian installation images are also distributed as smaller image files suitable for USB flash drives and similar removable devices. Because Debian CD and DVD images are created in an isohybrid format, they can boot from either optical disc drives or USB drives. As a result, the simplest method of preparing a USB memory stick is to download a CD or DVD image that fits on the device and write it directly to the stick, an action that erases any existing data on the device.


=== Network installation ===
A network installation, or "netinst", image is a single CD or DVD that allows installation of the entire operating system. It contains only the minimal software required to install the base system, and the remaining packages are fetched over the Internet during installation. In later releases, such as "Trixie", the netinst image includes the components needed to run the Debian Installer along with the base packages required for a minimal system, while users who prefer not to rely on a network connection during installation can instead use a full DVD image.


=== Live images ===

In addition to the standard installation images, Debian offers live images. A live image contains a complete Debian system that can be booted without modifying any files on the computer's storage, and it also allows Debian to be installed directly from the contents of the image. Live images are offered for the stable and testing suites and are available in several flavors, each offering a different desktop environment, including GNOME, KDE Plasma, Xfce, LXQt, LXDE, Cinnamon, and MATE. Live images are provided only for the amd64 architecture. They include the Calamares Installer, a distribution-independent installer framework intended to be easy for end users to operate. The images do not contain a complete set of language support packages, so users who require input methods, fonts, or other supplemental packages for their language must install these separately afterward. Live images are suitable for users who wish to try a Debian system and then install it from the same media, and they can be written to a USB flash drive or to DVD-R(W) media.


=== Cloud images ===
Debian provides virtual machine images that can be provisioned through service calls, configured and manipulated with manual or automated tools, and terminated when no longer needed. It supports several cloud-oriented use cases, including running as a guest operating system on various services, running the infrastructure that hosts a private cloud, and running as a client that interacts with cloud services through APIs or other network services.
Debian publishes official virtual machine images for the following cloud environments and marketplaces:

Amazon Web Services, through the AWS Marketplace
Microsoft Azure, through the Azure Marketplace
OpenStack, using generic images for the "Trixie" and "Bookworm" releases
Unofficial or third party images are also available. For example, Google publishes images for Google Compute Engine that include software and APT repositories not included in Debian.


=== Network booting ===
Installation over a local network is also supported through network booting. In this method, a TFTP server and a DHCP, BOOTP, or RARP server are configured to serve installation media to client machines on the network. If a client machine's BIOS supports the Preboot Execution Environment (PXE), it can boot the Debian installation system over the network using PXE and TFTP, after which the remainder of the installation proceeds over the network.


=== Verifying downloads ===
To verify the integrity and authenticity of downloaded images, official Debian installation and live images are accompanied by signed checksum files, located alongside the images in directories such as iso-cd, jigdo-dvd, and iso-hybrid. The checksums allow users to confirm that an image was not corrupted during download, while the digital signatures on the checksum files allow users to confirm that the image was created and released by Debian and has not been tampered with.


== Packages ==
Debian builds distributions of pre-compiled, freely licensed binary packages and distributes them through its archive. Packages generally contain all of the files necessary to implement a set of related commands or features. There are two types of Debian packages: binary packages and source packages.
Binary packages contain executables, configuration files, man pages, copyright information, and other documentation. These packages are distributed in a Debian-specific archive format and are typically identified by the file extension ".deb". Binary packages can be unpacked using the Debian utility dpkg, or through a front end such as apt.
Source packages consist of a .dsc file describing the source package, including the names of associated files, an .orig.tar.gz file containing the original, unmodified source in gzip compressed tar format, and, typically, a .debian.tar.xz file containing the Debian specific changes to the original source. The utility dpkg-source is used to pack and unpack Debian source archives. The program apt-get can also be used as a front end for dpkg-source.
Installation of software through the package system relies on dependencies, which are defined by package maintainers and documented in the control file associated with each package. For example, the package containing the GNU Compiler Collection (gcc) depends on the binutils package, which includes the linker and assembler. If a user attempts to install gcc without first installing binutils, the package management system (dpkg) reports an error indicating that binutils is also required and halts installation of gcc.
Debian's packaging tools support a range of functions, including manipulating and managing packages or their components, administering local overrides of files within them, assisting developers in building package archives, and helping users install those residing on a remote archive site.

 
Multiple tools are used to manage Debian packages, ranging from graphical or text-based interfaces to lower-level utilities used for direct package installation. All of them depend on these lower-level utilities to function properly. For example, aptitude and synaptic rely on apt, which in turn relies on dpkg to manage packages on the system.


=== Repositories ===
A Debian repository is a set of Debian binary or source packages organized in a special directory tree, with various infrastructure files (checksums, indices, signatures, descriptions, translations, and so on) added. Client computers can connect to the repository to download and install packages using an APT-based package management tool.
A Debian repository contains several releases. Debian releases are named after characters from the Toy Story franchise. The codenames have aliases according to their maturity stage, known as suites (stable, oldstable, testing, and unstable). A release is divided into several components. In Debian these are named main, non-free-firmware, contrib, and non-free, and they indicate the licensing terms of the software they contain. A release also has packages for various architectures, as well as sources and architecture-independent packages.
The root directory of a repository has a directory called dists, which in turn has a directory for each release and suite. The suite directory is usually a symlink to the release directory, but this is not visible when browsing. Each release subdirectory contains a cryptographically signed Release file and a directory for each component. Inside these are directories for the different architectures, named binary-<arch> and source. Within these are files named Packages, which are text files containing the metadata of packages. The actual packages are stored elsewhere.
The packages themselves are located below pool in the root directory of the repository. Below pool there are again directories for all the components, and within these are directories named 0 through 9, a through z, and liba through libz. These contain directories named after the software package they belong to, and these directories finally contain the actual packages, that is, the .deb files. The name is not necessarily the name of the package itself. For example, the package bsdutils resides in the pool/main/u/util-linux directory, named after the source package from which it is generated. A single upstream source may generate several binary packages, and all of them end up in the same subdirectory below pool. The additional single-letter directories are a way to avoid having too many entries in a single directory, which is a known performance problem for many file systems.
In the leaf directories below pool there are usually several versions of a package, and information about which releases each version belongs to resides solely in the indices. This way, the same version of a package can belong to several releases while using disk space only once, without resorting to hard links or symbolic links, which allows mirroring to remain simple and to work even with systems that lack these concepts.


==== Components ====
A repository may be divided into one or more of these components, and users might not choose to use all of them. Debian repositories generally include the following components:

main: Packages that comply with the Debian Free Software Guidelines (DFSG) and depend only on other DFSG-compliant packages. Only these packages are considered part of Debian proper.
contrib: DFSG-compliant packages that depend on packages that do not comply with the DFSG.
non-free: Packages that do not comply with the DFSG but are considered important enough to be made available anyway. One example is widely used fonts with unusual licensing requirements.
non-free-firmware: Non-DFSG-compliant firmware packages, such as those for network cards. These have been included by default since the release of Debian 12 "Bookworm".


== Branches ==
Three branches of Debian (also called releases, distributions or suites) are regularly maintained:

stable is the current release and targets stable and well-tested software needs. stable is made by freezing testing for a few months to fix bugs and remove packages with too many bugs; then the resulting system is released as stable. It is updated only for major security or usability fixes. This branch has an optional backporting service that provides more recent versions of some software.
testing is the preview branch that eventually becomes the next major release. The packages included in this branch have had some testing in unstable but may not be ready for release yet. It contains newer packages than stable but older than unstable. This branch is updated continually until it is frozen.
unstable, always codenamed "Sid", is the trunk. Packages are accepted without checking the distribution as a whole. This branch is usually run by software developers who participate in a project and need the latest libraries available, and by those who prefer bleeding-edge software.
Other branches in Debian:

oldstable is the prior stable release. It is supported by the Debian Security Team for one year after a new stable is released, and then for another two years through the Long Term Support project. Eventually, oldstable is moved to a repository for archived releases.
experimental is a temporary staging area of highly experimental software that is likely to break the system. It is not a full distribution and missing dependencies are commonly found in unstable, where new software without the damage risk is normally uploaded.
The snapshot archive provides older versions of the branches. They may be used to install a specific older version of some software.


=== Numbering scheme ===
stable and oldstable get minor updates, called point releases. The numbering scheme for the point releases up to Debian 4.0 "Etch" was to include the letter r (for revision) after the main version number and then the number of the point release; for example, the latest point release of version 4.0 is 4.0r9. This scheme was chosen because a new dotted version would make the old one look obsolete and vendors would have trouble selling their CDs.
From Debian 5.0 "Lenny", the numbering scheme of point releases was changed, conforming to the GNU version numbering standard; the first point release of Debian 5.0 was 5.0.1 instead of 5.0r1. The numbering scheme was once again changed for the first Debian 7 "Wheezy" update, which was version 7.1. The r scheme is no longer in use, but point release announcements include a note about not throwing away old installation media.


== Hardware ==
Hardware requirements are at least those of the kernel and the GNU toolsets. Debian's recommended system requirements depend on the level of installation, which corresponds to increased numbers of installed components:

The real minimum memory requirements depend on the architecture and may be much less than the numbers listed in this table. It is possible to install Debian with 170MB of RAM for x86-64; the installer will run in low memory mode and it is recommended to create a swap partition. The installer for z/Architecture requires about 20MB of RAM, but relies on network hardware. Similarly, disk space requirements, which depend on the packages to be installed, can be reduced by manually selecting the packages needed.
It is possible to run graphical user interfaces on older or low-end systems. However, installing window managers instead of desktop environments is recommended, as desktop environments use more resources. Requirements for individual software vary widely and must be considered, with those of the base operating environment.


=== Architectures ===
As of 9 August 2025, the "Trixie" release, the instruction set architecture officially supported are:

amd64: x86-64 64-bit
arm64: ARMv8 64-bit
armel: ARMv5 32-bit for use on legacy embedded systems (support dropped from unstable on 2025-11-03)
armhf: ARMv7 32-bit, requires a floating-point unit
ppc64el: PowerPC 64-bit for use with POWER7+ and POWER8 CPUs
riscv64: RISC-V 64-bit
s390x: z/Architecture 64-bit
Unofficial ports are available as part of the unstable distribution:

alpha: DEC Alpha
hppa: HP PA-RISC
hurd-i386: GNU Hurd kernel on IA-32
hurd-amd64: GNU Hurd kernel on x86-64
i386: IA-32 32-bit, compatible with x86 machines
loong64: LoongArch
mips64el: MIPS 64-bit
m68k: Motorola 68k on Amiga, Atari, Macintosh and various embedded VME systems
powerpc: PowerPC 32-bit
sh4: Hitachi SuperH
sparc64: Sun SPARC 64-bit
x32: x32 ABI for x86-64
Debian supports a variety of ARM-based network-attached storage (NAS) devices. The NSLU2 was supported by the installer in Debian 4.0 and 5.0, and Martin Michlmayr is providing installation tarballs since version 6.0. Other supported NAS devices are the Buffalo Kurobox Pro, GLAN Tank, Thecus N2100 and QNAP Turbo Stations.
Devices based on the Kirkwood system on a chip (SoC) are supported too, such as the SheevaPlug plug computer and OpenRD products. There are efforts to run Debian on mobile devices, but this is not a project goal yet since the Debian Linux kernel maintainers would not apply the needed patches. Nevertheless, packages exist for resource-limited systems.
There are efforts to support Debian on wireless access points. Debian is known to run on set-top boxes. Work is ongoing to support the AM335x processor, which is used in electronic point of service solutions. Debian may be customized to run on cash machines. BeagleBoard, a low-power open-source hardware single-board computer made by Texas Instruments, has switched to Debian Linux preloaded on its Beaglebone Black board's flash. Roqos Core, a x86-64 based IPS firewall router, runs on Debian Linux.


== Organization ==

Debian's policies and team efforts focus on collaborative software development and testing processes. As a result, a new major release tends to occur every two years with revision releases that fix security issues and important problems. The Debian project is a volunteer organization with two foundation documents:

The Debian Social Contract defines a set of basic principles by which the project and its developers conduct affairs.
The Debian Free Software Guidelines define the criteria for "free software" and thus what software is permissible in the distribution. These guidelines have been adopted as the basis of The Open Source Definition. Although this document can be considered separate, it formally is part of the Social Contract.
The Debian Constitution describes the organizational structure for formal decision-making within the project, and enumerates the powers and responsibilities of the Project Leader, the Secretary and other roles.

Debian developers are organized in a web of trust. There are about one thousand active Debian developers, but it is possible to contribute to the project without being an official developer.
The project maintains official mailing lists and conferences for communication and coordination between developers. For issues with single packages and other tasks, a public bug tracking system is used by developers and end users. Internet Relay Chat is also used for communication among developers and to provide real time help.
Debian is supported by donations made to organizations authorized by the leader. The largest supporter is Software in the Public Interest, the owner of the Debian trademark, manager of the monetary donations and umbrella organization for various other community free software projects.
A Project Leader is elected once per year by the developers. The leader has special powers, but they are not absolute, and appoints delegates to perform specialized tasks. Delegates make decisions as they think is best, taking into account technical criteria and consensus. By way of a General Resolution, the developers may recall the leader, reverse a decision made by the leader or a delegate, amend foundation documents and make other binding decisions. The voting method is based on the Schulze method (Cloneproof Schwartz Sequential Dropping).

Project leadership is distributed occasionally. Branden Robinson was helped by the Project Scud, a team of developers that assisted the leader, but there were concerns that such leadership would split Debian into two developer classes. Anthony Towns created a supplemental position, Second In Charge (2IC), that shared some powers of the leader. Steve McIntyre was 2IC and had a 2IC himself.
One important role in Debian's leadership is that of a release manager. The release team sets goals for the next release, supervises the processes and decides when to release. The team is led by the next release managers and stable release managers. Release assistants were introduced in 2003.


=== Developers ===
The Debian Project has an influx of applicants wishing to become developers. These applicants must undergo a vetting process which establishes their identity, motivation, understanding of the project's principles, and technical competence. This process has become much harder throughout the years.
Debian developers join the project for many reasons. Some that have been cited include:

Debian is their main operating system and they want to promote Debian
To improve the support for their favorite technology
They are involved with a Debian derivative
A desire to contribute back to the free software community
To make their Debian maintenance work easier
Debian developers may resign their position at any time, or when deemed necessary, they can be expelled. Those who follow the retiring protocol are granted emeritus status and may regain their membership via a shortened new member process.
Debian has made efforts to diversify and have members represented from the community. Debian Women in 2004 was established with the aim of having more women involved in development. Debian also partnered with Outreachy, which offers internships to individuals with underrepresented identities in technology.


== Development ==

Each software package has a maintainer that may be either one person or a team of Debian developers and non-developer maintainers. The maintainer keeps track of upstream releases, and ensures that the package coheres with the rest of the distribution and meets the standards of quality of Debian. Packages may include modifications introduced by Debian to achieve compliance with Debian Policy, even to fix non-Debian specific bugs, although coordination with upstream developers is advised.
The maintainer releases a new version by uploading the package to the "incoming" system, which verifies the integrity of the packages and their digital signatures. If the package is found to be valid, it is installed in the package archive into an area called the pool and distributed every day to hundreds of mirrors worldwide. As of April 5, 2025, there were a total of 379 Debian mirrors operating. The upload must be signed using OpenPGP-compatible software. All Debian developers have individual cryptographic key pairs. Developers are responsible for any package they upload even if the packaging was prepared by another contributor.
Initially, an accepted package is only available in the unstable branch. For a package to become a candidate for the next release, it must migrate to the testing branch by meeting the following:

It has been in unstable for a certain length of time that depends on the urgency of the changes.
It does not have "release-critical" bugs, except for the ones already present in testing. Release-critical bugs are those considered serious enough that they make the package unsuitable for release.
There are no outdated versions in unstable for any release ports.
The migration does not break any packages in testing.
Its dependencies can be satisfied by packages already in testing or by packages being migrated at the same time.
The migration is not blocked by a freeze.
Thus, a release-critical bug in a new version of a shared library on which many packages depend may prevent those packages from entering testing, because the updated library must meet the requirements too. From the branch viewpoint, the migration process happens twice per day, rendering testing in perpetual beta.
Periodically, the release team publishes guidelines to the developers in order to ready the release. A new release occurs after a freeze, when all important software is reasonably up-to-date in the testing branch and any other significant issues are solved. At that time, all packages in the testing branch become the new stable branch. Although freeze dates are time-based, release dates are not, which are announced by the release managers a couple of weeks beforehand.
A version of a package can belong to more than one branch, usually testing and unstable. It is possible for a package to keep the same version between stable releases and be part of oldstable, stable, testing and unstable at the same time. Each branch can be seen as a collection of pointers into the package "pool" mentioned above.
One way to resolve the challenge of a release-critical bug in a new application version is the use of optional package managers. They allow software developers to use sandbox environments, while at the same time remaining in control of security. Another benefit of a cross-distribution package manager is that they allow application developers to directly provide updates to users without going through distributions, and without having to package and test the application separately for each distribution.


=== Release cycle ===
A new stable branch of Debian is released about every 2 years. It will receive official support for about 3 years with update for major security or usability fixes. Point releases will be available every several months as determined by Stable Release Managers (SRM).
Debian also launched its Long Term Support (LTS) project since Debian 6 "Squeeze". For each Debian release, it will receive two years of extra security updates provided by LTS Team after its End Of Life (EOL). However, no point releases will be made. Now each Debian release can receive 5 years of security support in total.


=== Security ===
The Debian project handles security through public disclosure. Debian security advisories are compatible with the Common Vulnerabilities and Exposures dictionary, are usually coordinated with other free software vendors and are published the same day a vulnerability is made public. There used to be a security audit project that focused on packages in the stable release looking for security bugs; Steve Kemp, who started the project, retired in 2011 but resumed his activities and applied to rejoin in 2014.
The stable branch is supported by the Debian security team; oldstable is supported for one year. Although Squeeze was not officially supported, Debian coordinated an effort to provide long-term support for IA-32 and x86-64 platforms, until February 2016, five years after the initial release. testing is supported by the testing security team, but does not receive updates in as timely a manner as stable. unstable's security is left for the package maintainers.
The Debian project offers documentation and tools to harden a Debian installation both manually and automatically. AppArmor support is available and enabled by default since Buster. Debian provides an optional hardening wrapper, and does not harden all of its software by default using gcc features such as PIE and buffer overflow protection, unlike operating systems such as OpenBSD, but tries to build as many packages as possible with hardening flags.


== Branding ==

Debian has two logos. The official logo (also known as open use logo) contains the well-known Debian swirl and is the visual identity of the Debian Project. A separate logo also exists for use by the Debian Project and its members only.
The Debian "swirl" logo was designed by Raul Silva in 1999 as part of a contest to replace the semi-official logo that had been used. The winner of the contest received an @Debian.org email address, and a set of Debian 2.1 install CDs for the architecture of their choice. Initially, the swirl was magic smoke arising from an also included bottle of an Arabian-style genie presented in black profile, but shortly after was reduced to the red smoke swirl for situations where space or multiple colours were not an option, and before long the bottle version effectively was superseded. There has been no official statement from the Debian project on the logo's meaning, but at the time of the logo's selection, it was suggested that the logo represented the magic smoke that made computers work.

One theory about the origin of the Debian logo is that Buzz Lightyear, the chosen character for the first named Debian release, has a swirl in his chin. Stefano Zacchiroli also suggested that this swirl is the Debian one. Buzz Lightyear's swirl is a more likely candidate as the codenames for Debian are names of Toy Story characters. The former Debian project leader Bruce Perens used to work for Pixar and is credited as a studio tools engineer on Toy Story 2 (1999).


== Institutional users ==
Debian is used by several institutions, such as many universities, NGOs and other non-profit organizations (including the Wikimedia Foundation), and commercial companies. It has even been used in space, in laptops on board the International Space Station.
Debian has been very helpful to numerous government agencies in the public sector, such as in the city of Munich, which used a Debian-based distribution in its LiMux initiative for the government computer migration to Linux. Schools in Extremadura and Andalusia (Spain) also utilized Debian-based systems (gnuLinEx and Guadalinex, respectively) to develop digital skills and open-source computing in schools. There are many other cases of usage of Debian-based distributions in education, such as the deployment of Skolelinux/Debian Edu in Norwegian schools. In addition, other public administrations use Linux systems indirectly based on Debian, such as French Gendarmerie, which uses Ubuntu-derived GendBuntu distribution.The Five Distros That Changed Linux


== Derivatives ==

Debian is one of the most popular Linux distributions, and many other distributions have been created from the Debian codebase. As of 2025, DistroWatch lists 141 active Debian derivatives. The Debian project provides its derivatives with guidelines for best practices and encourages derivatives to merge their work back into Debian.
Among the most notable of these distributions are Ubuntu, developed by Canonical and first released in 2004, which has surpassed Debian in popularity with desktop users; Knoppix, first released in the year 2000 and one of the first distributions optimized to boot from external storage; Tails, a distribution focused on privacy and security first released in 2009 and now part of the Tor Project, known especially among journalists after Edward Snowden used it during his 2013 disclosures; and Devuan, which gained attention in 2014 when it forked in disagreement over Debian's adoption of the systemd software suite, and has been mirroring Debian releases since 2017. The Linux Mint Debian Edition has used Debian stable as the software source base since 2014.


=== Flavors ===
Debian Pure Blends are subsets of a Debian release configured out-of-the-box for users with particular skills and interests. For example, Debian Jr. is made for children, while Debian Science is for researchers and scientists. The complete Debian distribution includes all available Debian Pure Blends. "Debian Blend" (without "Pure") is a term for a Debian-based distribution that strives to become part of mainstream Debian, and have its extra features included in future releases.


==== Debian GNU/Hurd ====

Debian GNU/Hurd is a flavor based on the Hurd kernel (which, in turn, runs on the GNU Mach microkernel), instead of the Linux kernel. Debian GNU/Hurd has been in development since 1998, and made a formal release in May 2013, with 78% of the software packaged for Debian ported to the GNU Hurd. Hurd is not yet an official Debian release, and is maintained and developed as an unofficial port. Debian GNU/Hurd is distributed as an installer CD (running the official Debian installer) or ready-to-run virtual disk image (Live CD, Live USB). The CD uses the IA-32 architecture, making it compatible with IA-32 and x86-64 PCs.


==== Debian GNU/kFreeBSD ====

Debian GNU/kFreeBSD is a discontinued Debian flavor. It used the FreeBSD kernel and GNU userland. The majority of software in Debian GNU/kFreeBSD was built from the same sources as Debian, with some kernel packages from FreeBSD. The k in kFreeBSD is an abbreviation for kernel, which refers to the FreeBSD kernel. Before discontinuing the project, Debian maintained i386 and amd64 ports. The last version of Debian kFreeBSD was Debian 8 "Jessie" RC3. Debian GNU/kFreeBSD was created in 2002. It was included in Debian 6.0 "Squeeze" as a technology preview, and in Debian 7 "Wheezy" as an official port. Debian GNU/kFreeBSD was discontinued as an officially supported platform as of Debian 8. Debian developers cited OSS, pf, jails, NDIS, and ZFS as reasons for being interested in the FreeBSD kernel. It has not been officially updated since Debian 8. However, starting in July 2019, the operating system continued to be maintained unofficially. As of July 2023, the development of Debian GNU/kFreeBSD has officially terminated due to the lack of interest and developers.


== See also ==

Armbian
Comparison of Linux distributions
Comparison of mobile operating systems
Debian version history
GNU variants
List of Debian project leaders
List of open source mobile phones
Mobian


== References ==


== Further reading ==
Coleman, E. Gabriella (2013). Coding Freedom: The Ethics and Aesthetics of Hacking. Princeton University Press. ISBN 978-0-691-14461-0.
Hertzog, Raphaël (2013). The Debian Administrator's Handbook. Freexian. ISBN 979-10-91414-03-6. Retrieved June 22, 2014.
Krafft, Martin F. (2005). The Debian System: Concepts and Techniques. No Starch Press. ISBN 978-1-59327-069-8.


== External links ==

Official website 
debian.org at the Wayback Machine (archived 2026-05-26)
Debian at DistroWatch
