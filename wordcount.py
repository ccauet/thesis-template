#!/usr/bin/env python

import os
import pexpect
import fnmatch
import datetime
import argparse
import pytz
from pytz import timezone

file_exclude_list = ['tests.tex', 'titlepage.tex']
dirs_exclude_list = ['figures', 'tikz']
file_to_write = 'private/wordcount.txt'

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
    if not any(dir_exclude in root for dir_exclude in dirs_exclude_list):
      for f in matched_files:
        tex_files.append([root, unicode(f)])
    # else:
    #   print "Ignoring all files in " + root
  return tex_files

if __name__ == "__main__":
  parser = argparse.ArgumentParser() #
  parser.add_argument('-s', '--silent', dest='silent', action='store_true', help='silent mode: suppress all output')
  parser.add_argument('-e', '--exclude-appendix', dest='excl_appendix', action='store_true', help='exclude appendix from wordcount')
  args = parser.parse_args()

  if args.excl_appendix:
    dirs_exclude_list.append('appendices')

  #cwd = os.getcwdu()
  cwd = os.path.dirname(os.path.realpath(__file__))
  if not args.silent:
    print "Counting words..."
  n_total = 0
  files = create_file_list(cwd)
  # get wordcount for all files in /private/content/; exceptions specified in file_exclude_list
  for r,f in files:
    # basename = os.path.basename(r)
    name = os.path.join(r,f)
    try:
      n = int(pexpect.run('/Library/TeX/texbin/texcount -sum=1,1,1,0,160,1,32 -brief -1 -utf8 "'+name+'"'))
    except ValueError:
      n = 0
    n_total += n
    if not args.silent:
      print f, n
  if not args.silent:
    print 'Total:', n_total
  with open(os.path.join(cwd,file_to_write), "a") as f:
    f.write(datetime.datetime.now(timezone('Europe/Berlin')).isoformat()+'\t'+str(n_total)+'\n')
