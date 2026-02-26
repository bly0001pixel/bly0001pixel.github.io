import random
n = 100
choice = random.randint(1,n)
guess = -1
num = 0
while True:
    num += 1
    if num > 20:
        print("You ran out of questions!")
    guess = int(input(f"Guess {num} = "))
    if guess < choice:
        print("Higher")
    elif guess > choice:
        print("Lower")
    else:
        print("You won!")
        break