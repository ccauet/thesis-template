#!/usr/bin/env python

import argparse
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DayLocator, AutoDateLocator, DateFormatter
import datetime
# import pytz
# from pytz import timezone

if __name__ == "__main__":
  parser = argparse.ArgumentParser() #
  parser.add_argument('-f', '--file', dest='inputfile', help='input file', required=True)
  parser.add_argument('-o', '--output', dest='outfile', help='output file', default="wordcount.pdf")
  args = parser.parse_args()

  data = np.genfromtxt(args.inputfile, dtype=None)

  locator = AutoDateLocator()
  years = YearLocator()
  months = MonthLocator()
  days = DayLocator() 
  date_format = DateFormatter('%d.%m.%Y')

  dates = [datetime.datetime.strptime(timestamp[0][:-13], '%Y-%m-%dT%H:%M:%S') for timestamp in data]
  words = np.array([q[1] for q in data])
  pages = words/400.

  fig, ax_left = plt.subplots()
  ax_left.plot_date(dates, words, 'b-', xdate=True)
  ax_left.set_ylabel('Word count')

  ax_right = ax_left.twinx()
  ax_right.set_ylabel('Approx. no. of pages', color='r')
  ax_right.set_ylim(0, 120)
  # ax_right.axhline(y=100, color='r')
  ax_right.plot_date(dates, pages, 'r-', xdate=True)
  for tl in ax_right.get_yticklabels():
      tl.set_color('r')

  # format the ticks on the x-axis
  ax_left.xaxis.set_major_locator(locator)
  ax_left.xaxis.set_minor_locator(locator)
  ax_left.xaxis.set_major_formatter(date_format)
  ax_left.autoscale_view()

  ax_left.fmt_xdata = DateFormatter('%Y-%m-%dT%H:%M:%S')
  ax_left.fmt_ydata = words
  ax_left.grid(True)

  fig.autofmt_xdate()
  # plt.show()
  plt.savefig(args.outfile)