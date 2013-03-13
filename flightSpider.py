# coding: UTF-8

import os,sys
import time
#import logging
import fetchFlightInfo
import db3

startPos = 0 #starter number
endPos = 5999 #ender number

def start():
	count = 0   # count
	c = open('flightID.txt') #store all the flight IDs
	#name = './data/'+str(int(time.time()))+'.txt'
	#print name
	#output = open (name,'ab')
	for line in c.readlines():
		ids= line.split(' ')
		for flightId in ids:			
			#print count,startPos,endPos
			if count >= int(startPos) and count < int(endPos):
				print "[%s,%s,%s]parse flightId:%s" %(startPos,endPos,count,flightId)
				try:
					res = fetchFlightInfo.fetchFlightInfo(flightId) #fetch flight Info
				except Exception:
					print "flightId %d has no data",flightId
				#print " the no.%d finished" % count
				#fetchFlightInfo.dictOutput(res) 
				db3.dbwrite(res)  #write the result into database		
				#output.write(str(res))  #write data into txt file
				time.sleep(0.1)
				count = count+1
			elif  count < int(endPos):				
				count =count+1
			else:
				print "Finished! Total number ",count					
				break   #finish spider

	c.close()
	#output.close()

if __name__ == "__main__":
	try:
		startPos = sys.argv[1]
		endPos = sys.argv[2]
	except:
		pass  #if don't loading number, use default ones
	finally:
		print "Spider will start from %s to %s." % (startPos,endPos)
		print "Start Now!"
		start()
