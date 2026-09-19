# Progress Chef

Cloned from https://en.wikipedia.org/wiki/Progress_Chef.

Wikipedia text is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Page id: 22561399.

Progress Chef (formerly Chef) is a configuration management tool written in Ruby and Erlang. It uses a pure-Ruby, domain-specific language (DSL) for writing system configuration "recipes". Chef is used to streamline the task of configuring and maintaining a company's servers, and can integrate with cloud-based platforms such as Amazon EC2, Google Cloud Platform, Oracle Cloud, OpenStack, IBM Cloud, Microsoft Azure, and Rackspace to automatically provision and configure new machines. Chef contains solutions for both small and large scale systems.


== Features ==
The user writes "recipes" that describe how Chef manages server applications and utilities (such as Apache HTTP Server, MySQL, or Hadoop) and how they are to be configured. These recipes (which can be grouped together as a "cookbook" for easier management) describe a series of resources that should be in a particular state: packages that should be installed, services that should be running, or files that should be written. These various resources can be configured to specific versions of software to run and can ensure that software is installed in the correct order based on dependencies. Chef makes sure each resource is properly configured and corrects any resources that are not in the desired state.
Chef can run in client/server mode, or in a standalone configuration named "chef-solo". In client/server mode, the Chef client sends various attributes about the node to the Chef server. The server uses Elasticsearch to index these attributes and provides an API for clients to query this information. Chef recipes can query these attributes and use the resulting data to help configure the node.
Traditionally, Chef was used to manage Linux but later versions add support for  Microsoft Windows.
It is one of the major configuration management systems on Linux, along with CFEngine, Ansible and Puppet. Along with Puppet and Ansible, it is a notable Infrastructure as Code (IAC) tool.


== History ==


=== Opscode ===
Chef was founded by Nathen Haneysmith, Adam Jacob and Barry Crist, and based in Seattle, United States. It operates as an Infrastructure automation platform for applications until today. 
In February 2013, Opscode released version 11 of Chef. Changes in this release included a complete rewrite of the core API server in Erlang.
In Sep 2015, Chef Chef was valued at $360 million after a $40 million  venture capital funding round.
In November 2015, the company acquired a German security startup, VulcanoSec.
In April 2019, the company announced that the source code for their software would continue to be released under the Apache 2.0 license, while binaries would only be available under the terms of a proprietary license. In response, the Cinc project began releasing Apache 2.0 licensed binaries of several Chef products.
In 2019, it was discovered by a journalist that U.S. Immigration and Customs Enforcement was paying Chef approximately $95,000 per year for a software license. At that time, a former Chef employee deleted his code repository in protest of the contract. The company did not announce any changes to its contracting processes or partners.


=== Chef Automate ===
Chef offered a single commercial product, Chef Automate, released at ChefConf in July 2016. Chef Automate included a full-stack continuous deployment pipeline, and automated testing for compliance and security. Chef Automate built on two of Chef's open source projects - Chef and InSpec - and integrated with the company's third open source project, Habitat. Habitat offered "application automation" to simplify running complex applications in different environments including containers, traditional data servers, or PaaS.
Chef offered three versions of its product: Chef Basics (free, open source), Hosted Chef ($72/node, minimum 20 node purchase), and Chef Automate ($137/node, annual subscription).


=== Progress ===
On September 8, 2020, Progress announced the acquisition of Chef, with an intended final date in October.
A press release gave the price of acquisition at $220 million. The merged company was named Progress Chef.


== Platform support ==
Chef is supported on multiple platforms according to a supported platforms matrix for client and server products. Major platform support for clients includes AIX, Amazon Linux, Debian, CentOS/RHEL, FreeBSD, macOS, Solaris, SUSE Linux, Microsoft Windows and Ubuntu. Additional client platforms include Arch Linux and Fedora. Chef Server is supported on amd64 on RHEL/CentOS, Oracle Linux, SUSE Linux and Ubuntu.


== See also ==

Comparison of open-source configuration management software
Infrastructure as code (IaC)
Infrastructure as Code Tools
Ansible (software)
CFEngine (software)
DevOps
DevOps toolchain
Puppet (software)
Salt (software)
Juju (software)


== References ==


== Further reading ==
Blogumas, Tj (15 April 2020). "Who killed the Chef? The case against Opscode Chef in 2020". DevOps Dudes.


== External links ==
Official website
