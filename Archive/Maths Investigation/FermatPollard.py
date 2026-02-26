import math, random, time

def Fermats_Factorisation(N):
    a = math.ceil(math.sqrt(N))

    while True:
        b = math.sqrt(a**2 - N)

        # Check if b is a whole number
        if b - math.floor(b) == 0:
            # Output p and q
            pq = [int(a - b), int(a + b)]
            pq.sort()
            return pq

        # Increment a and retry
        else:
            a += 1

def PollardRho(N):
    x = (random.randint(0, N - 2))
    y = x
    c = (random.randint(0, N - 1))
    d = 1

    # Repeat until GCD of |x-y| and N != 1
    while (d == 1):
    
        # Tortoise Move: x(i+1) = f(x(i)) 
        x = (pow(x, 2, N) + c) % N

        # Hare Move: y(i+1) = f(f(y(i))) 
        y = (pow(y, 2, N) + c) % N
        y = (pow(y, 2, N) + c) % N

        # Check gcd of |x-y| and N 
        d = math.gcd(abs(x - y), N)

        # Retries algorithm if |x-y| = 0 and therfore GCF of 0 and N = N
        if (d == N):
            return PollardRho(N)
        
    # Output p and q
    pq = [int(d),int(N/d)]
    pq.sort()
    return pq

def test(trial):
    timeFSum = 0
    timePSum = 0
    timeFCount = 0
    timePCount = 0

    for i in range(5):
        N, p, q = trial

        startTimeF = time.time()
        resultsF = Fermats_Factorisation(N)
        if resultsF[0] == p and resultsF[1] == q:
            endTimeF = time.time()
            timeFSum += endTimeF - startTimeF
            timeFCount += 1

        startTimeP = time.time()
        resultsP = PollardRho(N)
        if resultsP[0] == p and resultsP[1] == q:
            endTimeP = time.time()
            timePSum += endTimeP - startTimeP
            timePCount += 1

    if timeFCount > 0 and timeFSum > 0:
        timeF = timeFSum / timeFCount
    else:
        timeF = 0
    if timePCount > 0 and timePSum > 0:
        timeP = timePSum / timePCount
    else:
        timeP = 0

    return timeF, timeP, p, q, N

testingData = []

with open("/home/jonathan-b/Documents/Python/Maths Investigation/FP_Input.csv", "r") as file:
    for line in file:
        line = line.strip().split(",")
        testingData.append([int(line[0]),int(line[1]),int(line[2])])

with open("/home/jonathan-b/Documents/Python/Maths Investigation/FP_Output.csv", "w") as file:
    for trial in testingData:
        timeF, timeP, p, q, N = test(trial)
        file.write(f"{timeF:.10f},{timeP:.10f},{p},{q},{N}\n") 

print("FINISHED")    