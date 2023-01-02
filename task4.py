import random

initNumber = random.randint(1, 1000)

print (initNumber)

binaryList = []

while initNumber > 0:
    divRes = divmod(initNumber, 2)
    binaryList.insert(0, divRes[1])
    initNumber = divRes[0]

print (''.join(map(str, binaryList)))