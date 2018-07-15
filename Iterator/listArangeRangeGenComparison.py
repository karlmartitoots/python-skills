import time
import numpy as np

n = 1000000

#numpy arange
sum = 0
startArange = time.time()
for i in np.arange(n):
    sum += 1
endArange = time.time()
arangeTime = endArange - startArange

startRange = time.time()
for i in range(n):
    sum += 1
endRange = time.time()
rangeTime = endRange - startRange

startList = time.time()
for i in [x for x in range(n)]:
    sum += 1
endList = time.time()
listTime = endList - startList

startGen = time.time()
for i in (x for x in range(n)):
    sum += 1
endGen = time.time()
genTime = endGen - startGen

print("Arange time: ", arangeTime)
print("Range time: ", rangeTime)
print("List time: ", listTime)
print("Gen time: ", genTime)