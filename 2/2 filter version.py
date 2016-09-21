# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 20:04:32 2016

@author: yihong

"""
import string

text = open('source.txt').read()

s = filter(lambda x: x in string.ascii_letters, text)
print s
