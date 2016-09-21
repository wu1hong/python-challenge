# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 20:57:59 2016

@author: yihong
"""

from PIL import Image
img = Image.open("oxygen.png")
#print img.size
#print img.getpixel((1,1))
#data = [img.getpixel((i, j)) for i in range(0, 609) for j in range(43, 53)]
'''data = []
data.extend(img.getpixel((i, j)) for i in xrange(0, 609) for j in xrange(43, 53))
print data '''
a = [chr(img.getpixel((i, 43))[0]) for i in range(0, 609, 7)]
print "".join(a)
b = [chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]]
print "".join(b)

#row = [chr(img.getpixel((i, 43))[0]) for i in range(0, 609, 9)]
#print row




