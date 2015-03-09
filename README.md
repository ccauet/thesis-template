# Thesis template

- Authors: Christophe Cauet (christophe@cauet.de), Florian Kruse
- Date: 2014-06-29

***How to work with this template***   
This thesis template is based on a private/common layout, i.e. large parts are shared between collaborators (config, definitions, references) while the main content is stored elsewhere. To work with this template, create a file hierarchy with the following minimal structure and create a symlink named ```private```
 pointing there. 

```
.
├── config
│   └── config.tex
├── content
│   ├── content.tex
│   └── titlepage
│       └── titlepage.tex
├── definitions
│   ├── abbreviations
│   │   └── abbreviations.tex
│   ├── acronyms
│   │   └── acronyms.tex
│   └── counter.tex
└── references
    └── bibliography.bib
```

To make use of ```%!TEX root = ..``` in your editor, create a second symlink called ```common``` in your private file hierarchy.

***git-annex***   
User guides for all used packages can be found in [doc/](/doc/) using [git-annex](http://git-annex.branchable.com).