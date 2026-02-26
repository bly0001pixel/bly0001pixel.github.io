import time, threading, os

frequency = 1000

script_dir = os.path.dirname(os.path.abspath(__file__))

registerMemory = [0, 0, 0, 0]
programMemory = [0 for _ in range(2 ** 9)]
programMemoryFilename = os.path.join(script_dir, "machinecode.txt")
mainMemory = [0 for _ in range(2 ** 10)]
flagRegisters = [0, 0]

programCounter = 0
phaseCounter = 0

aluFlags = [False, False]

decodedData = [0, 0, 0]
decodedEW = 0

def to_signed_int(x):
    if isinstance(x, str):
        v = int(x, 2) & 0xFF
    else:
        v = int(x) & 0xFF
    if v & 0x80:
        return v - 0x100
    return v

def to_unsigned(x):
    if isinstance(x, str):
        return int(x, 2) & 0xFF
    return int(x) & 0xFF

def splitStr(s, len1, len2):
    return s[:len1], s[len1:len1+len2]

def readProgramMemory(filename):
    with open(filename, "r") as f:
        content = f.read().strip()
        if not content:
            return
        for i, instr in enumerate(content.split()):
            if instr.strip() == "":
                continue
            programMemory[i] = int(instr) & 0x1FF

def fetch(pc):
    return format(programMemory[pc] & 0xFF, "08b")

def decode(instBin="00000000", AorI=0, W2="00"):
    global programCounter
    if AorI == 1:
        programCounter += 1
        AL = format(programMemory[programCounter] & 0xFF, "08b")
        AH = W2
        addr = int(AH + AL, 2)
        return 0, 0, mainMemory[addr]
    elif AorI == 2:
        programCounter += 1
        return 0, 0, programMemory[programCounter]
    else:
        opcode, nib2 = splitStr(instBin, 4, 4)
        opcode = int(opcode, 2)
        if opcode in [0, 1, 15]:
            return [opcode, nib2[:2], nib2[2:]], 0, 0
        elif opcode in [2, 6, 8, 10, 11]:
            R0, R1 = splitStr(nib2, 2, 2)
            return [opcode, R0, R1], 0, 0
        elif opcode in [3, 5]:
            R0, AH = splitStr(nib2, 2, 2)
            return [opcode, R0, AH], 1, AH
        elif opcode in [4]:
            R0, UN = splitStr(nib2, 2, 2)
            return [opcode, R0, 0], 2, 0
        elif opcode in [12, 13, 14]:
            return [opcode, 0, 0], 2, 0
        elif opcode in [7, 9]:
            R0, UN = splitStr(nib2, 2, 2)
            return [opcode, R0, 0], 0, 0

def alu(op, a, b):
    global aluFlags
    sa = to_signed_int(a)
    sb = to_signed_int(b)
    if op == 0:
        result = (sa + sb) & 0xFF
    elif op == 1:
        result = (sa - sb) & 0xFF
    elif op == 2:
        ua = to_unsigned(a)
        ub = to_unsigned(b)
        result = (~(ua & ub)) & 0xFF
    elif op == 3:
        ua = to_unsigned(a)
        ub = to_unsigned(b)
        result = (~(ua | ub)) & 0xFF
    aluFlags[0] = (result == 0)
    aluFlags[1] = ((result & 0x80) != 0)
    return result

def execute(data, EW):
    global programCounter
    opcode, d1, d2 = data
    d1i = int(d1, 2) if isinstance(d1, str) else d1
    d2i = int(d2, 2) if isinstance(d2, str) else d2
    if opcode == 0:
        return
    elif opcode == 1:
        quit()
    elif opcode == 2:
        registerMemory[d1i] = registerMemory[d2i]
    elif opcode == 3:
        registerMemory[d1i] = EW
    elif opcode == 4:
        registerMemory[d1i] = EW
    elif opcode == 5:
        mainMemory[EW & 0x3FF] = registerMemory[d1i]
    elif opcode == 6:
        registerMemory[d1i] = alu(0, registerMemory[d1i], registerMemory[d2i])
    elif opcode == 7:
        registerMemory[d1i] = alu(0, registerMemory[d1i], 1)
    elif opcode == 8:
        registerMemory[d1i] = alu(1, registerMemory[d1i], registerMemory[d2i])
    elif opcode == 9:
        registerMemory[d1i] = alu(1, registerMemory[d1i], 1)
    elif opcode == 10:
        registerMemory[d1i] = alu(2, registerMemory[d1i], registerMemory[d2i])
    elif opcode == 11:
        registerMemory[d1i] = alu(3, registerMemory[d1i], registerMemory[d2i])
    elif opcode == 12:
        programCounter = EW & 0x1FF
    elif opcode == 13:
        if not aluFlags[0]:
            programCounter = EW & 0x1FF
    elif opcode == 14:
        if not aluFlags[1]:
            programCounter = EW & 0x1FF
    elif opcode == 15:
        opcode2 = (d1i << 2) | d2i
        if opcode2 == 0:
            os.system("clear")
        elif opcode2 == 1:
            print(f"REG A = {to_signed_int(registerMemory[0])}")
        elif opcode2 == 2:
            print(f"REG B = {to_signed_int(registerMemory[1])}")
        elif opcode2 == 3:
            print(f"REG C = {to_signed_int(registerMemory[2])}")
        elif opcode2 == 4:
            print(f"REG D = {to_signed_int(registerMemory[3])}")
        elif opcode2 == 5:
            print(f"REG A = {to_signed_int(registerMemory[0])}")
            print(f"REG B = {to_signed_int(registerMemory[1])}")
            print(f"REG C = {to_signed_int(registerMemory[2])}")
            print(f"REG D = {to_signed_int(registerMemory[3])}")
        elif opcode2 == 6:
            print(f"Z FLAG = {aluFlags[0]}")
        elif opcode2 == 7:
            print(f"N FLAG = {aluFlags[1]}")

def main():
    global phaseCounter, programCounter, instruction, decodedData, decodedEW
    if phaseCounter == 0:
        instruction = fetch(programCounter)
    elif phaseCounter == 1:
        decodedData, AorI, W2 = decode(instBin=instruction)
        if AorI > 0:
            _, _, decodedEW = decode(AorI=AorI, W2=W2)
        else:
            decodedEW = 0
    elif phaseCounter == 2:
        execute(decodedData, decodedEW)
    phaseCounter = (phaseCounter + 1) % 3
    if phaseCounter == 0:
        programCounter = (programCounter + 1) & 0x1FF

def clock(frequency, callback):
    period = 1 / frequency
    while True:
        callback()
        time.sleep(period)

def run():
    readProgramMemory(programMemoryFilename)
    t = threading.Thread(target=clock, args=(frequency, main), daemon=True)
    t.start()
    while True:
        pass