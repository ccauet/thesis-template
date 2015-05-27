#!/usr/bin/env python

#
# Prettify TeX/Tikz plots from ROOT
#
# Usage:
#  prettify_pgfplots.py plotfile [dictfile]
#  
# The plot is in TeX/Tikz format requring several strings and patterns to be 
# replaced. The dictionary needs to be supplied as valid Python code that can be
# imported by this script. 
#

import fileinput, re, sys, imp, os

def prettify_file(filename, dictfiles):
  replaces = []

  replace_dict = {}
  for dictfile in dictfiles:
    replace = imp.load_source('replace_dict', dictfile)
    replace_dict.update(replace.replace_dict)

  first_line = ""
  with open(filename, 'r') as f:
    first_line = f.readline()
  if "tikzpicture" not in first_line and "\pgf" not in first_line:
    print "File " + filename + " not a Tikz plot."
    return
  
  for l in fileinput.input(filename, inplace=True):
    line = l
    for regex, subst in replace_dict.iteritems():
      (s, num) = re.subn(regex, subst, line)
      if num>0:
        line = s
    print line,

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "Usage: " + __file__ + " plotfile [dictfiles]"
    sys.exit(1)

  plotfile = sys.argv[1]
  dictfiles = ""
  if len(sys.argv) >= 3:
    dictfiles = sys.argv[2:]
  else:
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    path_private = os.path.join(os.path.dirname(os.path.dirname(path)), os.path.join("private", "scripts"))
    dictfiles = []
    if os.path.exists(os.path.join(path, "prettify_dictionary.py")):
      dictfiles.append(os.path.join(path, "prettify_dictionary.py"))
    if os.path.exists(os.path.join(path_private, "prettify_dictionary.py")):
      dictfiles.append(os.path.join(path_private, "prettify_dictionary.py"))  

  prettify_file(plotfile, dictfiles)