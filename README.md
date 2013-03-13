filghtest (China)
=========

this project aims to estimate the flight delay of chinese airplane companies.

Step one:
we will use web spider to fetch public info from veryzhun.com and get structured data in following format:
	{'status':'准点，飞机目前抵达深圳'            //the final status of one certain flight
	,'accuracyRate':'93.33%'                     //avg accuracy rate 
	,'planeID':'ZH9992'                          //flight ID
	,'rArriveTime':'11:56'                       //Real arrive time
	,'from':'合肥'                               //start city
	,'fVisibility':'能见度9999米'                //the visibility of start airport  
	,'rTakeOffTime':'10:09'                      //Real take off time
	,'company':'深圳航空公司'                    //plance owner Info
	,'tVisibility':'能见度7000米'                //visibility of destination artport
	,'fTemp':'24℃'                             // Temperature of start city
	,'fWeather':'晴天'                          // weather of start city
	,'planeType':'737-800'                      // plane type
	,'to':'深圳B区'                             //destination    
	,'tairportCondition':'机场流量正常。'       //air traffic condition of desination airport 
	,'eTakeOffTime':'09:50'                    //estimate take off time
	,'fAirportCondition':'机场小面积延误。'     //air traffic condition of taking-off airport 
	,'tWeather':'多云'                         //weather of destinate city  
	,'pArriveTime':'11:50'                     //plan arrive time    
	,'tTemp':'23℃'                            //Temperature of destination 
	,'eArriveTime':'11:50'                     //estimate arrive time
	,'pTakeOffTime':'09:50'}                   //planed take off time


/////////////////////////////////////////////////////////////////////////////////////////////////////////
2013-03-21
fixed several bugs:
1. handle exceptions when spider deal empty contents
2. store the data into mysql db instead of txt files
3. allow set start position when start spider

