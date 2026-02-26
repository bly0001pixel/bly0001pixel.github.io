import random

max = 12

allFactors = []

def summate(list):
    total = 0
    for item in list:
        total += item
    return total

for i in range(1000):
    test = []
    for i in range(10):
        test.append(random.randint(1,12))
    total = summate(test)
    if total == 64:
        allFactors.append(test)
        print(f"{test}, {total}")
