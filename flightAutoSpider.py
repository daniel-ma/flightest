#!/bin/usr/python
# coding:utf-8

import time
from datetime import datetime,date,timedelta
import MySQLdb
import dbInfo
import fetchFlightInfo
import db3


def startPerHour(): #check last two hour landed airplane
	timeNow = time.strftime("%H:%M",time.localtime())# just keep hour and minute ,delete date info here
	timeNow = datetime(* time.strptime(timeNow,"%H:%M")[:6]) # transfer date str into datetime format
	timeSin= timeNow+timedelta(hours=-2) # time of 2 hours before
	try: #conn to db
		conn = MySQLdb.connect(host=dbInfo.DBLOC,user=dbInfo.DBUSER,passwd=dbInfo.DBPASS,db=dbInfo.DBSCHEMA,charset='utf8')
	except:
		print "could not connect to the db server now! please try again"
		exit(0)
	try:
		cur = conn.cursor()
		sql = "select plane_id from schedule where depart_time between %s and %s" 
		values = [timeSin,timeNow]
		count = cur.execute(sql,values)
		for i in range(0,count):
			cres = cur.fetchone()
			flightId = cres[0] #get plane_id
			#print "parse flightId:%s" % flightId
			try:
				res = fetchFlightInfo.fetchFlightInfo(flightId) #fetch flight Info
			except Exception:
				print "flightId %s has no data"% flightId
			db3.dbwrite(res)
			time.sleep(0.2)
		print "Finished! Total amount=",count
			
	except Exception,e:
		print e.args[0]

	cur.close()
	conn.close()

startPerHour()
