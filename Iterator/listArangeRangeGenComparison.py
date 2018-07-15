import time
import numpy as np

def getTime(iterable, moreTime = 0):
    sum = 0
    start_time = time.time()
    for i in iterable:
        sum += 1
    return moreTime + time.time() - start_time

def printer(dataObject,result):
    print(dataObject + " time: " + str(result))

n = 100000000

#iterable creation times
arangeStart = time.time()
myArange = np.arange(n)
arangeTime = time.time() - arangeStart

rangeStart = time.time()
myRange = range(n)
rangeTime = time.time() - rangeStart

listStart = time.time()
myList = [x for x in range(n)]
listTime = time.time() - listStart

genStart = time.time()
myGen = (x for x in range(n))
genTime = time.time() - genStart

print("Arange time: ", getTime(np.arange(n),moreTime = arangeTime))
print("Range time: ", getTime(range(n),moreTime = rangeTime))
print("List time: ", getTime(myList,moreTime = listTime))
print("Gen time: ", getTime(myGen,moreTime = genTime))

