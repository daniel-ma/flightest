#!/bin/usr/python
#coding=utf-8

# this program is used to update the 'schedule' table in database to record the regular depart and land time of all airplanes in China. Those data will be used to guide our spider operate automatically.
#Author: Daniel Ma 
#Time  : 2013-03-21

import time
import MySQLdb
import datetime
import dbInfo

def update(dateNow='2013-03-14'):
	try:
		conn = MySQLdb.connect(host=dbInfo.DBLOC,user=dbInfo.DBUSER,passwd=dbInfo.DBPASS,db=dbInfo.DBSCHEMA,charset='utf8')
	except:
		print "could not connect to the db server now! please try again"
		exit(0)
	
	#dateNow=date.today()
	try:
		cur=conn.cursor()
		sql = "select plane_id,p_take_off_time,p_arrive_time from landingrecord where date=%s"
		values = [dateNow]
		count=cur.execute(sql,values)
		cur2=conn.cursor()
		for i in range(0,count):
			res = cur.fetchone()
			replace_sql="replace into schedule(plane_id,depart_time,land_time,date) values(%s,%s,%s,%s)"
			departTime= ''
			arriveTime= '0000-00-00 00:00:00'
			try:
				departTime=datetime.datetime(* time.strptime(res[1],"%H:%M")[:6])
				arriveTime=datetime.datetime(* time.strptime(res[2],"%H:%M")[:6])
			except:
				pass
			values=[res[0],departTime,arriveTime,dateNow]
			cur2.execute(replace_sql,values)
			#print "replace %d succeed!" % i
		conn.commit()
	except MySQLdb.Error,e:
		print "mysql error %d:%s"% e.args[0],e.args[1]
	except Exception,e:
		print "[Error]: ",e.args[0]
	cur.close()
	cur2.close()
	conn.close()

update()
