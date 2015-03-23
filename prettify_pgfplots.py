#!/usr/bin/env python

#
# Prettify TeX/Tikz plots from ROOT
#
# Usage:
#  prettify_pgfplots.py plotfile dictfile
#  
# The plot is in TeX/Tikz format requring several strings and patterns to be 
# replaced. The dictionary needs to be supplied as valid Python code that can be
# imported by this script. 
#

import fileinput, re, sys, imp

def prettify_file(filename, dictfile):
  replace = imp.load_source('replace_dict', dictfile)

  for l in fileinput.input(filename, inplace=True):
    line = l
    for regex, subst in replace.replace_dict.iteritems():
      (s, num) = re.subn(regex, subst, line)
      if num>0:
        line = s
    print line,

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "Usage: " + __file__ + " plotfile dictfile"
    sys.exit(1)

  plotfile = sys.argv[1]
  dictfile = sys.argv[2]

  filename = "obsMass_{dd;t}_pull_log.tex"
  prettify_file(plotfile, dictfile)