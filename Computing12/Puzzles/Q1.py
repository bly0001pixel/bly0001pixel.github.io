fingers = ["Thumb", "First Finger", "Middle Finger", "Ring Finger", "Little Finger", "Ring Finger", "Middle Finger", "First Finger"]
for i in range(100):
    n = i
    output = fingers[(n % len(fingers))]
    print(n+1)
    print(output)