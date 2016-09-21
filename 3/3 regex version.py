# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 19:51:35 2016

@author: yihong
"""
import re

text = open('1.txt').read()
a = "".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',text))
print a