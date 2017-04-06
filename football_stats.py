#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: football_stats.py."""


from bs4 import BeautifulSoup
import csv
import urllib2
import argparse


if __name__ == "__main__":
    count = 0
    url = "http://www.cbssports.com/nfl/stats/playersort/nfl/year-2016-season-regular-category-touchdowns"
    response = urllib2.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, "html5lib")

    ofile = open("football_stats.csv", "w")
    f = csv.writer(ofile)
    f.writerow(["Player", "Pos", "Team", "TD"])

    trs = soup.find_all('tr')
    for tr in trs:
        tds = tr.find_all("td")
        try:
            name = str(tds[0].get_text())
            pos = str(tds[1].get_text())
            team = str(tds[2].get_text())
            td = str(tds[6].get_text())
        except:
            continue
        f.writerow([name, pos, team, td])
        count = count + 1
        if count == 20:
            break

    ofile.close()
