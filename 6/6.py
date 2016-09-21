# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 22:21:19 2016

@author: yihong
"""

import re, zipfile

text = "Next nothing is "
number = "90052"
search = re.compile("(\d*)$")
z = zipfile.ZipFile("channel.zip")
comments = []
match = ["90052"]

while True:
    if number == '':
        break
    f = open("D:/Program Save/python challenge/6/channel/"+number+".txt").read()
    comments.append(z.getinfo(number+".txt").comment)
    print f
    match = search.findall(f)
    number = match[0]
    print number
    
    

a = "".join(comments)
b = open("1.txt",'w')
b.write(a)
b.close()

    