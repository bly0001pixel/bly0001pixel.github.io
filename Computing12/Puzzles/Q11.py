n = 10000
counts = [0 for i in range(9)]
for i in range(n):
    power = 2**(i+1)
    powerSL = list(str(power))
    counts[int(powerSL[0])-1] += 1

frequencies = []
for i, count in enumerate(counts):
    frequencies.append(f"{i} = {str(round(count / n * 100))}%")

print(frequencies)
