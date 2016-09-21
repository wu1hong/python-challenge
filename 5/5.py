# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 22:08:12 2016

@author: yihong
"""
import urllib
import pickle

url = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
data = pickle.loads(url)
a = ""
for each in data:
    a +="".join(i[0] * i[1] for i in each)
f = open("channel.txt", 'w')
f.write(a)
f.close()