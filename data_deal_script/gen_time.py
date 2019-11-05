import time
import random

'''
a = "2013-10-10 23:40:00"
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S") 
timeStamp = int(time.mktime(timeArray)) 
print timeStamp
'''



timeStamp = random.randint(1,1544572800)
for x in xrange(1,100):
	timeArray = time.localtime(timeStamp)
	otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray) 
	print otherStyleTime
	timeStamp += 1
	