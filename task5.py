import random

counter = random.randint(1, 10)
negaFibo = [1, 0, 1]

print(counter)

while counter > 1:
    negaFibo.insert(0, negaFibo[1] - negaFibo[0])
    negaFibo.append(negaFibo[len(negaFibo) - 2] + negaFibo[len(negaFibo) - 1])
    counter = counter - 1

print(negaFibo)