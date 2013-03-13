filghtest (China)
=========

this project aims to estimate the flight delay of chinese airplane companies.

Step one:
we will use web spider to fetch public info from veryzhun.com and get structured data in following format:
	{'status':'׼�㣬�ɻ�Ŀǰ�ִ�����'            //the final status of one certain flight
	,'accuracyRate':'93.33%'                     //avg accuracy rate 
	,'planeID':'ZH9992'                          //flight ID
	,'rArriveTime':'11:56'                       //Real arrive time
	,'from':'�Ϸ�'                               //start city
	,'fVisibility':'�ܼ���9999��'                //the visibility of start airport  
	,'rTakeOffTime':'10:09'                      //Real take off time
	,'company':'���ں��չ�˾'                    //plance owner Info
	,'tVisibility':'�ܼ���7000��'                //visibility of destination artport
	,'fTemp':'24��'                             // Temperature of start city
	,'fWeather':'����'                          // weather of start city
	,'planeType':'737-800'                      // plane type
	,'to':'����B��'                             //destination    
	,'tairportCondition':'��������������'       //air traffic condition of desination airport 
	,'eTakeOffTime':'09:50'                    //estimate take off time
	,'fAirportCondition':'����С�������'     //air traffic condition of taking-off airport 
	,'tWeather':'����'                         //weather of destinate city  
	,'pArriveTime':'11:50'                     //plan arrive time    
	,'tTemp':'23��'                            //Temperature of destination 
	,'eArriveTime':'11:50'                     //estimate arrive time
	,'pTakeOffTime':'09:50'}                   //planed take off time


/////////////////////////////////////////////////////////////////////////////////////////////////////////
2013-03-21
fixed several bugs:
1. handle exceptions when spider deal empty contents
2. store the data into mysql db instead of txt files
3. allow set start position when start spider

