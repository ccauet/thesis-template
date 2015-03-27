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
  args = parser.parse_args()

  data = np.genfromtxt(args.inputfile, dtype=None)

  locator = AutoDateLocator()
  years = YearLocator()
  months = MonthLocator()
  days = DayLocator() 
  date_format = DateFormatter('%d.%m.%Y')

  dates = [datetime.datetime.strptime(timestamp[0][:-13], '%Y-%m-%dT%H:%M:%S') for timestamp in data]
  words = [q[1] for q in data]

  

  fig, ax = plt.subplots()
  ax.plot_date(dates, words, '-', xdate=True)
  ax.set_ylabel('Word count')

  # format the ticks
  ax.xaxis.set_major_locator(locator)
  ax.xaxis.set_minor_locator(locator)
  ax.xaxis.set_major_formatter(date_format)
  ax.autoscale_view()

  ax.fmt_xdata = DateFormatter('%Y-%m-%dT%H:%M:%S')
  # ax.fmt_ydata = words
  ax.grid(True)

  fig.autofmt_xdate()
  # plt.show()
  plt.savefig("wordcount.pdf")