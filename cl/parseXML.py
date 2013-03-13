#!/bin/usr/python
# coding: UTF-8


from bs4 import BeautifulSoup
import re

class ParseXML:
    def __init__(self,content):
        self.content = content.decode('UTF-8')

#  parse the veryzhun.com/fnumber/num + flightID page
#  Stucture analysis , may need to update frequently if the page changed
    def parseVeryZhunFnumber(self):
        #pattern = re.compile(u"预计起飞时间.w*(?=</p>)")
        #res = pattern.search(self.content)
        #print res
        soup = BeautifulSoup(self.content)
        tags=soup.find_all(re.compile("ul"))
        #store the result info into a dictionary
        res = {}
        res['from']=tags[0].text
        
	#weather and temperature 
	tag1 = tags[1].find_all('li')
	wt=tag1[0].div
	res['fTemp']=wt.text
        pattern = re.compile("(?<=alt=\")[^x00-xff]*(?=\")")
	weather= pattern.search(str(wt))	
	if weather :
		 res['fWeather'] = weather.group().decode('UTF-8') #utf8 into unicode

        #sight visibility
	if len(tag1) > 1:
		res['fVisibility'] = tag1[1].text
	
	#airport status
	if len(tag1) > 2:
		res['fAirportCondition'] = tag1[2].text

	#airplane number	
	if len(tags) > 2: res['planeID'] = tags[2].text	

	#airplane owner Info
	tags3 =tags[3].find_all('a')
	if len(tags) > 3:  
		res['company'] = tags3[1].text
		res['planeType'] = tags3[3].text
	
	#history accuracy rate
	historyRate= tags[3].br   #<br>历史准点率：93.33%</br>
	pattern  = re.compile('\d*\.\d*%')
	rate = pattern.search(str(historyRate))
	if rate:
		res['accuracyRate'] =rate.group()

	#destination airport
	res['to']=tags[4].text

	
	#weather and temperature 
	tag5 = tags[5].find_all('li')
	wt=tag5[0].div
	res['tTemp']=wt.text
        pattern = re.compile("(?<=alt=\")[^x00-xff]*(?=\")")
	weather= pattern.search(str(wt))	
	if weather :
		 res['tWeather'] = weather.group().decode('UTF-8') #utf8 into unicode

        #sight visibility
	if len(tag5) > 2:
		res['tVisibility'] = tag5[1].text
 		res['tairportCondition'] = tag5[2].text	#airport status
	
	#test ouput in chinese words	
	#print '{'+','.join(map(lambda kv_pair:"'%s':'%s'" % kv_pair, res.iteritems()))+'}'
	return res

    #update the real arrive time of one plane
    def updateTimeOnVeryZhun(self):
	soup = BeautifulSoup(self.content)
	#time info , examples shows below
	#<p>计划起飞时间：09:50</p>, <p>预计起飞时间：09:50</p>, <p>实际起飞时间：09:55</p>, <p>飞机状态：<span class="red">已经到达</span></p>, <p class="planestate">准点，飞机目前抵达深圳</p>, <p>计划到达时间：11:50</p>, <p>预计到达时间：11:50</p>, <p>实际到达时间：11:49</p>, <p style="clear:both"></p>
	timeSource = soup.find_all('p')     #find all <p></p> tag
	timePattern = re.compile('\d{0,2}:\d{0,2}')   #get time like 09:50
	res = {}
	if len(timeSource) > 8:
		sr = timePattern.search(str(timeSource[0]))
		if sr: res['pTakeOffTime'] = sr.group() #planed take off time
		sr = timePattern.search(str(timeSource[1]))
		if sr: res['eTakeOffTime'] = sr.group()  #estimate take off time	
		sr = timePattern.search(str(timeSource[2]))
		if sr: res['rTakeOffTime'] = sr.group() # real take off time
		res['status'] = timeSource[4].text
		sr = timePattern.search(str(timeSource[5]))
		if sr: res['pArriveTime'] = sr.group() # planed arrive time
		
		sr = timePattern.search(str(timeSource[6]))
		if sr: res['eArriveTime'] = sr.group() # estimate arrive time
		
		sr = timePattern.search(str(timeSource[7]))
		if sr :  res['rArriveTime'] = sr.group() # real arrive time
	#test ouput in chinese words	
	#print '{'+','.join(map(lambda kv_pair:"'%s':'%s'" % kv_pair, res.iteritems()))+'}'
	return res

def main():
    c = open('res.txt')
    XML = c.read()
    parseXML = ParseXML(XML)
    parseXML.parseVeryZhunFnumber()
    parseXML.updateTimeOnVeryZhun()


if __name__ == '__main__':
    main()
