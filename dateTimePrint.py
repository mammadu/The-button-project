# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:42:57 2019

@author: muham
"""

import datetime

hts = 3600 #this is a constant for converting hours to seconds
mts = 60 #this is a constant for converting minutes to seconds

#this marks the beginning of the procrastination session
startTime = datetime.datetime.now() 

input ("Press enter to continue")

#this marks the ending of the procrastination session
endTime = datetime.datetime.now()

#the next two lines are for debugging purposes. They print out startTime and endTime

#print ("First time was ", startTime)
#print ("Second time was ",  endTime)

startTimeInSeconds = startTime.hour*hts + startTime.minute*mts + startTime.second
endTimeInSeconds = endTime.hour*hts + endTime.minute*mts + endTime.second


secondOfDay = [] #this array represents each second of the day.

i = 0 #this int is to create elements in the array secondOfDay
x = 0 #this is a counter for each second in the array secondOfDay
for i in range(0,60*60*24):
    secondOfDay.append(x)
    i+=1

#the next line shows the length of the array secondOfDay. 
#This length shouyld equal 86400 which is the number of seconds in a day

#print("length of array secondOfDay is ", len(secondOfDay))
    

 
for s in range (startTimeInSeconds, endTimeInSeconds):
     secondOfDay[s] += 1
     
     
  #Need to relate date and day of month to second of day.