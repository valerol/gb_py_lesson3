import random

myList = []
mySum = 0

for i in range(0, 10):
    myList.append(round(random.uniform(0, 10), 3))

    if i == 1 or i % 2 != 0:
        mySum += myList[i]

print(myList)
print("odd element sum: " + str(mySum))