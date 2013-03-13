#/bin/usr/python
#encoding=UTF-8

import logging
import MySQLdb
from datetime import date 

DBLOC="192.168.1.104"
DBUSER="root"
DBPASS="RooT"
DBSCHEMA="airplane"

def dbwrite(dic):  #write the dictionary result into db 
	try:
		db=MySQLdb.connect(host=DBLOC,user=DBUSER,passwd=DBPASS,db=DBSCHEMA,charset='utf8')
	except:
		print "could not connect to MYSQL server"
		exit(0)    
	dateNow=date.today() 
	try:
		sql=u"replace into landingrecord (status,accuracy_rate,plane_id,r_arrive_time,`from`,f_visibility \
		,f_temp,f_weather,plane_type,`to`,t_airport_condition,e_take_off_time,f_airport_condition \
		,t_weather,p_arrive_time,t_temp,e_arrive_time,p_take_off_time \
		,date) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') " % (dic.get('status'),dic.get('accuracyRate'),dic.get('planeID'),dic.get('rArriveTime'),dic.get('from'),dic.get('fVisibility'),dic.get('fTemp'),dic.get('fWeather'),dic.get('planeType'),dic.get('to'),dic.get('tairportCondition'),dic.get('eTakeOffTime'),dic.get('fAirportCondition'),dic.get('tWeather'),dic.get('pArriveTime'),dic.get('tTemp'),dic.get('eArriveTime'),dic.get('pTakeOffTime'),dateNow)
	#print sql.encode('utf-8')
	
		cur = db.cursor()
		cur.execute(sql.encode('utf-8'))
		db.commit()
		cur.close()
	except MySQLdb.Error,e:
		print "mysql error %d:%s" %(e.args[0],e.args[1])
		#exit(0)
	except Exception,e:
		print "Error happend! %s" % e.args[0]
	finally:
		db.close()
