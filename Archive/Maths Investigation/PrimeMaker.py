import random

def stripLine(line):
    return line.strip()

with open("/home/jonathan-b/Documents/Python/Maths Investigation/primes1.txt", "r") as file:
    text = file.read()
    primes = [int(prime) for prime in text.split() if prime.strip()]

with open("/home/jonathan-b/Documents/Python/Maths Investigation/FP_Input.csv", "w") as file:
    
    limit = 1000000
    count = 3000
    
    for i in range(count):
        prime1, prime2 = limit + 1, limit + 1
        while prime1 > limit:
            prime1 = primes[random.randint(0,len(primes)-1)]
        while prime2 > limit:
            prime2 = primes[random.randint(0,len(primes)-1)]
        semiprime = prime1 * prime2
        prime12 = [prime1, prime2]
        prime12.sort()
        file.write(f"{semiprime},{prime12[0]},{prime12[1]}\n")

    print("FINISHED")