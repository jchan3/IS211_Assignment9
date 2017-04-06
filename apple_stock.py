#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: apple_stock.py."""


from bs4 import BeautifulSoup
import csv
import urllib2
import argparse


if __name__ == "__main__":
    count = 0
    urlstr = "http://chart.finance.yahoo.com/table.csv?s=AAPL&a=9&b=1&c=2016&d=9&e=31&f=2016&g=d&ignore=.csv"

    try:
        response = urllib2.urlopen(urlstr)
        reader = csv.reader(response)
    except urllib2.HTTPError as e:
        print "The server could not fulfill the request."
        print "Error code: ", e.code
    except urllib2.URLError as e:
        print "We failed to reach a server."
        print "Reason: ", e.reason

    ofile = open("apple_stock.csv", "w")
    f = csv.writer(ofile)

    for line in reader:
        date = line[0]
        close_price = line[4]
        f.writerow([close_price, date])

    ofile.close()
