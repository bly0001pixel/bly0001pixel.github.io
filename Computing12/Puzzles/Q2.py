list = [10,2,25,32,100,7,17,33,8,64]
sList = []

for i in range(len(list)):
    smallest = 99999999999999999999999999999999999999999999999999
    for item in list:
        if item < smallest:
            smallest = item
    list.remove(smallest)
    sList.append(smallest)

print(sList)