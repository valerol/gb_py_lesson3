import random
import math

initList = []
resList = []

for i in range(0, random.randint(5, 10)):
    initList.append(random.randint(0, 10))

for i in range(0, math.ceil(len(initList)/2)):
    resList.append(initList[i] * initList[len(initList) -1 - i])

print (initList)
print (resList)