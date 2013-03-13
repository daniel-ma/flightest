# coding: UTF-8

import time
#import logging
import fetchFlightInfo


count = 0   # count
c = open('flightID.txt')
name = './data/'+str(int(time.time()))+'.txt'
print name
output = open (name,'ab')
print "start the fetch now!"
for line in c.readlines():
	ids= line.split(' ')
	for flightId in ids:
		print "parse flightId:",flightId
		res = fetchFlightInfo.fetchFlightInfo(flightId) #fetch flight Info
		#print " the no.%d finished" % count
		print fetchFlightInfo.dictOutput(res) 
		time.sleep(0.1)
		count +=1
	if count >2:
		break

c.close()
output.close()
