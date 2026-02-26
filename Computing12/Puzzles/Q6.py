n = 8
if n > 2:
    men = [i+1 for i in range(n)]
    for i in range(n):
        print(f"{men}, {i}")
        if len(men) > 2:
            killed = men.pop((i+1)%len(men))
        else:
            killed = men.pop(-1 if n % 2 != 0 else 0)
        print(f"{killed} died")
        if len(men) == 1:
            break
    print(men[0])
else:
    print(n-1)