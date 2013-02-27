#!/bin/usr/python

import urllib2
import re
# one html parse plug-ins
from bs4 import BeautifulSoup 

c = urllib2.urlopen('http://www.veryzhun.com/fnumber/num/ZH9992.html')

soup = BeautifulSoup(c.read())

target = soup.find_all('div',class_='numdap')[0].parent
#target2 = soup.find_all('div',class_='numinfo')
#target3 = soup.find_all('div',class_='numarr')

output = open('res.txt','a')
output.write(str(target))
output.close()
