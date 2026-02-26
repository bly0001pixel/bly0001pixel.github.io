import time

tape = [0,0,0]
index = 1
halted = False
rule = 0

rules = [
    [[1, "Left", 1], ["HALT"]],
    [[0, "Right", 0], [0, "Right", 0]]
]

def left():
    tape.insert(0, 0)

def right():
    global index
    tape.append(0)
    index += 1

while not halted:
    read = tape[index]
    if rules[rule][read][0] != "HALT":
        tape[index] = rules[rule][read][0]
        if rules[rule][read][1] == "Right":
            right()
        else:
            left()
        rule = rules[rule][read][2]
    else:
        halted = True

    time.sleep(1)