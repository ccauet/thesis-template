# Thesis template

- Authors: Christophe Cauet (christophe@cauet.de), Florian Kruse (pa@floriankru.se)

***How to work with this template***   
This thesis template is based on a private/common layout, i.e. large parts are shared between collaborators (config, definitions, references) while the main content is stored elsewhere. To work with this template, you should create a file hierarchy with the following minimal structure and create a symlink named ```private``` pointing there. 

```
.
└── content
    └── content.tex
```

In case you want to include private configurations, definitions, a title page, or an appendix, the minimal template can be extended.

```
.
├── config
│   └── config.tex
├── content
│   ├── appendices
│   │   └── appendices.tex
│   ├── content.tex
│   └── titlepage
│       └── titlepage.tex
└── definitions
    ├── abbreviations
    │   └── abbreviations.tex
    ├── acronyms
    │   └── acronyms.tex
    └── definitions.tex
```

To make use of ```%!TEX root = ..``` in your editor, create a second symlink called ```common``` in your private file hierarchy.

***git-annex***   
User guides for all used packages can be found in [doc/](/doc/) using [git-annex](http://git-annex.branchable.com).

Useful fonts can be found in [fonts/](/fonts/) using [git-annex](http://git-annex.branchable.com).

## Font setup

The directory [common/config/fonts/](/common/config/fonts/) contains sets of matching fonts that can be activated with a simple include in your own ```private/config/``` setup.

## Rapid mode

To speed up compilation, rapid mode can be enabled by defining rapidmode as true in the ```private/config/``` setup:

```
\rapidmode
```

This currently has the following effects:

1. Tikz externalize library is used to avoid unnecessary recompilation of Tikz figures
2. Todonotes are disabled (not compatible with Tikz externalize)

Other speed-up features might be added in the future.

### Caveats – rapid mode

Compilation with ```latexmk``` in SublimeText/LaTeXTools does not work with externalize as the ```-shell-escape``` option is not propagated to ```lualatex```. To fix this add the following to your LaTeXTools user settings:

```
{
…
	"builder_settings" : {	
		// General settings:
		// See README or third-party documentation
		"program": "lualatex",
		"command": ["latexmk", "-cd", "-e", "$pdflatex = '%E -shell-escape -interaction=nonstopmode -synctex=1 %S %O'", "-f", "-pdf"],

		// (built-ins): true shows the log of each command in the output panel
		"display_log" : false,	

		// Platform-specific settings:
		"osx" : {
			// See README or third-party documentation
		},

		"windows" : {
			// See README or third-party documentation

		},

		"linux" : {
			// See README or third-party documentation
		}
	},
…
}
```

## Todo notes

Todos can be defined with the following macros:

```
\todo{Do something}
\important{Do something ASAP!}
\info{A rather informational todo note.}
\missing{Add section about interesting study}
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

## Special LHCb content

Special [LHCb](http://lhcb-public.web.cern.ch/lhcb-public/) content can be found in ```definitions/acronyms/lhcb.tex``` and ```references/lhcb.bib```. The acronyms can be added to the private configuration by adding the line:

```
\input{common/definitions/acronyms/lhcb}
```

or for the LHCb-centric bibliography:

```
\addbibresource{common/references/lhcb.bib}
```
