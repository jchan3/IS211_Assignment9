#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: weather.py."""


from bs4 import BeautifulSoup
import csv
import urllib2
import argparse


if __name__ == "__main__":
    count = 0
    url = "https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html"
    response = urllib2.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, "html5lib")

    ofile = open("weather.csv", "w")
    f = csv.writer(ofile)
    f.writerow(["Date", "Avg Temp"])

    trs = soup.find_all('tr')
    for tr in trs:
        tds = tr.find_all("td")
        try:
            avg = str(tds[2].get_text())
            count += 1
        except:
            continue
        if count > 10:
            f.writerow([count-10, avg])

    ofile.close()
