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

## Todo notes

Todos can be defined with the following macros:

```
\todo{Do something}
\important{Do something ASAP!}
\info{A rather informational todo note.}
\addref{Note for a missing reference.}
\replace{this}{by that}
\redo{Recreate this ugly looking plot and make it nice!}
```

All todos can be disabled by adding 
```
\presetkeys{todonotes}{disable}{}
```
to the private config files.

To make todos inline by default:
```
\presetkeys{todonotes}{inline}{}
```

## Scripts

***[wordcount.py](wordcount.py)***   
Create word count for all files in [private/content/](/private/content) and write log file including timestamp to [private/](/private/).
_Dependencies_: [texcount](http://app.uio.no/ifi/texcount/) and the python modules: os, [pexpect](https://pexpect.readthedocs.org/en/latest/), fnmatch, datetime, [pytz](http://pytz.sourceforge.net)

***[common/scripts/plot_wordcount.py](common/scripts/plot_wordcount.py)***   
Script to parse and plot the word count log file. _Dependencies_: argparse, numpy, matplotlib, datetime

***[common/scripts/prettify_pgfplots.py](common/scripts/prettify_pgfplots.py)***   
Utility to "prettify" tikz-based plots from ROOT. Based on a python dictionary with regexps (if not specified, this is ```common/scripts/prettify_dictionary.py```) patterns will be replaced by proper TeX code (e.g. broken particle names by proper symbols).
_Dependencies_: Python modules: fileinput, re, sys, imp, os

***[common/scripts/prettify_all.py](common/scripts/prettify_all.py)***   
Prettify all tikz-based plots. Will be run via make.
_Dependencies_: Python modules: os, [pexpect](https://pexpect.readthedocs.org/en/latest/), fnmatch, datetime, [pytz](http://pytz.sourceforge.net)
