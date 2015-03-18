#!/usr/bin/env python

import os
import pexpect
import fnmatch
import datetime
import argparse
import pytz
from pytz import timezone

file_exclude_list = ['tests.tex', 'titlepage.tex']
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
    for f in matched_files:
      tex_files.append([root, f])
  return tex_files

if __name__ == "__main__":
  parser = argparse.ArgumentParser() #
  parser.add_argument('-s', '--silent', dest='silent', action='store_true', help='silent mode: suppress all output')
  args = parser.parse_args()

  #cwd = os.getcwdu()
  cwd = os.path.dirname(os.path.realpath(__file__))
  if not args.silent:
    print "Counting words..."
  n_total = 0
  files = create_file_list(cwd)
  # get wordcount for all files in /private/content/; exceptions specified in file_exclude_list
  for r,f in files:
    n = int(pexpect.run('/usr/texbin/texcount -sum=1,1,1,0,0,1,16 -brief -1 -utf8 '+r+'/'+f))
    n_total += n
    if not args.silent:
      print f, n
  if not args.silent:
    print 'Total:', n_total
  with open(os.path.join(cwd,file_to_write), "a") as f:
    f.write(datetime.datetime.now(timezone('Europe/Berlin')).isoformat()+'\t'+str(n_total)+'\n')
