# path:/home/zilliz/workspace/develop
# coding=utf-8


import random
import datetime
import time

dataCount = 100   # 10.
codeRange = range(ord('a'), ord('z'))
alphaRange = [chr(x) for x in codeRange]
alphaMax = len(alphaRange)
daysMax = 42003
theDay = datetime.date(1900, 1, 1)
timeStamp = random.randint(1,1544572800)


def genRandomName(nameLength):  #generate string
    global alphaRange, alphaMax
    length = random.randint(1, nameLength)
    name = ''
    for i in range(length):
        name += alphaRange[random.randint(0, alphaMax - 1)]
    return name


def genRandomDay():   #generate  birthday
    global daysMax, theDay
    mDays = random.randint(0, daysMax)
    mDate = theDay + datetime.timedelta(days=mDays)
    return mDate.isoformat()


def genRandomTime(timeStamp):  #generate  time
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray) 
    return otherStyleTime


def genRandomSex():
    return random.randint(0, 1)


def genDataBase1(fileName, dataCount):
    outp = open(fileName, 'w')
    i = 0
    while i < dataCount:
        time = genRandomTime(timeStamp + i)
        firstName = genRandomName(14)
        lastName = genRandomName(14)
        birthday = genRandomDay()
        sex = genRandomSex()
        mLine = "%i %s %s %s %s %d\n" % (
            i + 1, time, firstName, lastName, birthday, sex)
        outp.write(mLine)
        i += 1
    outp.close()

if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase1('db_test.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
