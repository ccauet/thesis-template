# Thesis template

- Authors: Christophe Cauet (christophe@cauet.de), Florian Kruse (pa@floriankru.se)

***How to work with this template***   
This thesis template is based on a private/common layout, i.e. large parts are shared between collaborators (config, definitions, references) while the main content is stored elsewhere. To work with this template, you should create a file hierarchy with the following minimal structure and create a symlink named ```private``` pointing there. 

```
.
├── config
│   └── config.tex
├── content
│   ├── content.tex
│   └── titlepage
│       └── titlepage.tex
└── definitions
    ├── abbreviations
    │   └── abbreviations.tex
    ├── acronyms
    │   └── acronyms.tex
    └── counter.tex
```

To make use of ```%!TEX root = ..``` in your editor, create a second symlink called ```common``` in your private file hierarchy.

***git-annex***   
User guides for all used packages can be found in [doc/](/doc/) using [git-annex](http://git-annex.branchable.com).

Useful fonts can be found in [fonts/](/fonts/) using [git-annex](http://git-annex.branchable.com).

## Font setup

The directory [common/config/fonts/](/common/config/fonts/) contains sets of matching fonts that can be activated with a simple include in your own ```private/config/``` setup.

## Script

***wordcount.py***   
Create word count for all files in [private/content/](/private/content) and writes log file including timestamp to [private/](/private/).
__Dependencies__: [texcount](http://app.uio.no/ifi/texcount/) and the python modules: os, [pexpect](https://pexpect.readthedocs.org/en/latest/), fnmatch, datetime, [pytz](http://pytz.sourceforge.net)
