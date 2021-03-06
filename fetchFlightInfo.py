#!/bin/usr/python
# coding: UTF-8

import urllib2
import re
# one html parse plug-ins
from bs4 import BeautifulSoup 
from cl import parseXML


# fetch flight info by flight ID ,such as 'ZH9992'
#input :
#      flightID, string type
#Output:
#      return a dictionary including all info received 
def fetchFlightInfo(flightID):
	url = 'http://www.veryzhun.com/fnumber/num/'+str(flightID)+'.html'
	#print url
	c = urllib2.urlopen(url)

	soup = BeautifulSoup(c.read())

	# target the useful data inside the page source
	target = soup.find_all('div',class_='numdap')[0].parent

	parse = parseXML.ParseXML(str(target))
	basicInfo= parse.parseVeryZhunFnumber()
	timeInfo = parse.updateTimeOnVeryZhun()
	entireInfo = dict(basicInfo.items() + timeInfo.items())
	dictOutput(entireInfo)
	return entireInfo

# standard output stream and show unicode in utf-8 format
#input : 
#      source , dictionary
#Output:
#      return the dicitionary as a utf-8 string
def dictOutput(source):
	 return '{'+','.join(map(lambda kv_pair:"'%s':'%s'" % kv_pair, source.iteritems()))+'}'


if __name__ == '__main__':
	fetchFlightInfo('ZH9992')	
