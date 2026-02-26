#Registers start at 0
#& AND, % MOVE TO, # NUMBER

#mov (Move: Reg1 To Reg2) {mvr Reg1%Reg2}
#add (Add: Reg1 + Reg2, Answer to Reg3) {add Reg1&Reg2}
#sub (Subtract: Reg1 - Reg2, Answer to Reg3) {sub Reg1&Reg2%Reg3}
#mlt (Multiply: Reg1 * Reg2, Answer to Reg3) {mlt Reg1&Reg2%Reg3}
#div (Divide: Reg1 / Reg2, Answer to Reg3) {div Reg1&Reg2%Reg3}
#ind (Power: Reg1 ^ Reg2, Answer to Reg3) {ind Reg1&Reg2%Reg3}
#rot (Root: Reg2 Root of Reg1, Answer to Reg3) {rot Reg1&Reg2%Reg3}
#prt (Print: Reg) {prt Reg}
#set (Set: Reg # Num) {set Reg#Num}
#ret (Returns: Num Lines) {ret Num}
#jic (Jump Compare: Num Lines If Reg1 > Reg2) {jic Reg1&Reg2#Num}
#jie (Jump Equal: Num Lines If Reg1 = Reg2) {jie Reg1&Reg2#Num}

def read_instructions(filename):
    readData = {}
    counter = 1
    with open(filename, "r") as file:
        for line in file:
            readData[counter] = line.strip()
            counter += 1
    return readData

def follow_instructions(instructions, registers, startLine):
    line_num = startLine
    
    while line_num <= len(instructions):
        line_num += 1
        
        if line_num - 1 not in instructions:
            print(f"Invalid line number: {line_num - 1}")
            break

        item = instructions[line_num - 1]
        commandSplit = item.split(" ")
        
        if len(commandSplit) != 2:
            print(f"Invalid instruction format at line {line_num - 1}: {item}")
            break

        command = commandSplit[0].strip()
        data = commandSplit[1].strip()

        if command == "mov":
            dataSplit = data.split("%")
            reg1 = int(dataSplit[0])
            reg2 = int(dataSplit[1])
            registers[reg2] = registers[reg1]
        
        elif command == "add":
            dataSplit = data.split("%")
            reg3 = int(dataSplit[1])
            addSplit = dataSplit[0].split("&")
            reg1 = int(addSplit[0])
            reg2 = int(addSplit[1])
            registers[reg3] = registers[reg1] + registers[reg2]

        elif command == "sub":
            dataSplit = data.split("%")
            reg3 = int(dataSplit[1])
            subSplit = dataSplit[0].split("&")
            reg1 = int(subSplit[0])
            reg2 = int(subSplit[1])
            registers[reg3] = registers[reg1] - registers[reg2]

        elif command == "mlt":
            dataSplit = data.split("%")
            reg3 = int(dataSplit[1])
            subSplit = dataSplit[0].split("&")
            reg1 = int(subSplit[0])
            reg2 = int(subSplit[1])
            registers[reg3] = registers[reg1] * registers[reg2]

        elif command == "div":
            dataSplit = data.split("%")
            reg3 = int(dataSplit[1])
            subSplit = dataSplit[0].split("&")
            reg1 = int(subSplit[0])
            reg2 = int(subSplit[1])
            registers[reg3] = registers[reg1] / registers[reg2]

        elif command == "ind":
            dataSplit = data.split("%")
            reg3 = int(dataSplit[1])
            subSplit = dataSplit[0].split("&")
            reg1 = int(subSplit[0])
            reg2 = int(subSplit[1])
            registers[reg3] = registers[reg1] ** registers[reg2]

        elif command == "rot":
            dataSplit = data.split("%")
            reg3 = int(dataSplit[1])
            subSplit = dataSplit[0].split("&")
            reg1 = int(subSplit[0])
            reg2 = int(subSplit[1])
            registers[reg3] = registers[reg1] ** (1/registers[reg2])
        
        elif command == "prt":
            reg = int(data)
            print(registers[reg])

        elif command == "set":
            dataSplit = data.split("#")
            reg1 = int(dataSplit[0])
            registers[reg1] = int(dataSplit[1])

        elif command == "ret":
            line_num -= int(data)
            continue

        elif command == "jic":
            dataSplit = data.split("#")
            num = int(dataSplit[1])
            jumpSplit = dataSplit[0].split("&")
            reg1 = int(jumpSplit[0])
            reg2 = int(jumpSplit[1])
            if registers[reg1] > registers[reg2]:
                line_num += num
                continue

        elif command == "jie":
            dataSplit = data.split("#")
            num = int(dataSplit[1])
            jumpSplit = dataSplit[0].split("&")
            reg1 = int(jumpSplit[0])
            reg2 = int(jumpSplit[1])
            if registers[reg1] == registers[reg2]:
                line_num += num
                continue

def main():
    registers = [0] * 20
    
    instructions = read_instructions("instructions.txt")
    follow_instructions(instructions, registers, 1)

if __name__ == "__main__":
    main()
