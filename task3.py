import random

initList = []
preparedList = []

for i in range(0, 10):
    initList.append(round(random.uniform(0, 10), 3))
    preparedList.append(round(initList[i] - int(initList[i]), 3))

preparedList.sort()

print(initList)
print(preparedList[len(preparedList) - 1] - preparedList[0]) 