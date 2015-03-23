#!/usr/bin/env python

import os
import pexpect
import fnmatch
import datetime
import argparse
import pytz
from pytz import timezone

file_exclude_list = ['tests.tex', 'titlepage.tex']

def create_file_list(cwd):
  tex_files = []
  for root, dirs, files in os.walk(cwd+'/private/content'):
    # only .tex files
    matched_files = fnmatch.filter(files, '*.tex')
    # remove all files from exclude list
    for f in file_exclude_list:
      if matched_files.count(f) > 0:
        matched_files.remove(f)
    # create tuple [root, filename]
    for f in matched_files:
      tex_files.append([root, unicode(f)])
  return tex_files

if __name__ == "__main__":
  #cwd = os.path.dirname(os.path.realpath(__file__))
  cwd = os.getcwd()
  files = create_file_list(cwd)
  # get wordcount for all files in /private/content/; exceptions specified in file_exclude_list
  for r,f in files:
    name = os.path.join(r,f)
    #print "Prettifying " + name
    output = pexpect.run('common/scripts/prettify_pgfplots.py "'+name+'"')
    if len(output)>0:
      print output,
