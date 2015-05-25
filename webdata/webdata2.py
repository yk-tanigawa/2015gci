#!/usr/bin/env python
# coding: utf-8

###################################################################
# Yahoo newsのタイトルを抽出して表示するスクリプト
# 2015.05.25 yk_tani
###################################################################

import urllib2
from xml.etree import ElementTree as etree

# rssを開く
target = 'http://rss.dailynews.yahoo.co.jp/fc/science/rss.xml'
rssfile = urllib2.urlopen(target)
data = rssfile.read()
rssfile.close()

# etreeでパース
root = etree.fromstring(data)
items = root.findall('channel/item')

# ニュースのタイトルを抽出
feed = []
for i in items:
    t = i.findtext('title')
    feed.append(t)

# 抽出したタイトルを表示
for i in feed:
    print i
