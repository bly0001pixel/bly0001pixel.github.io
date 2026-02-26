'''
for n in range(20):
    h = 0
    days = 0

    while True:
        h += 3
        days += 1
        if h < n:
            h -= 2
        else:
            break
'''

n = int(input("n = "))
print(f"{max(1, n-2)} days")
