import os

script_dir = os.path.dirname(__file__)
inputname = os.path.join(script_dir, "assemblycode.txt")
outputname = os.path.join(script_dir, "machinecode.txt")

opcodes = {
    "NOP":"0000", #0
    "HLT":"0001", #0
    "MOV":"0010", #RR
    "LDA":"0011", #RA
    "LDI":"0100", #RI
    "STR":"0101", #RA
    "ADD":"0110", #RR
    "INC":"0111", #R
    "SUB":"1000", #RR
    "DEC":"1001", #R
    "NND":"1010", #RR
    "NOR":"1011", #RR
    "JMP":"1100", #I
    "JNZ":"1101", #I
    "JNN":"1110", #I
    "OUT":"1111", #0
}

registers = {
    "A":"00",
    "B":"01",
    "C":"10",
    "D":"11"
}

outOpcode = {
    "CLR":"0000",
    "A":"0001",
    "B":"0010",
    "C":"0011",
    "D":"0100",
    "ALL":"0101",
    "Z":"0110",
    "N":"0111"
}

def splitStr(s, len1, len2):
    part1 = s[:len1]
    part2 = s[len1:len1+len2]
    return part1, part2

def run():
    data = "0 "
    with open(inputname, "r") as file:
        for line in file:
            if line.strip():
                databin1 = ""
                databin2 = ""
                splitComment = line.strip().split("#")
                split = splitComment[0].strip().split(" ")
                databin1 += opcodes[split[0]]
                if split[0] in ["NOP", "HLT"]: #0
                    databin1 += "0000"
                elif split[0] in ["OUT"]: #OUT
                    databin1 += outOpcode[split[1]]
                elif split[0] in ["INC", "DEC"]: #R
                    databin1 += registers[split[1]]
                    databin1 += "00"
                elif split[0] in ["LDA", "STR"]: #RA
                    databin1 += registers[split[1]]
                    H, L = splitStr(format(int(split[2]), "010b"), 2, 8)
                    databin1 += H
                    databin2 = L
                elif split[0] in ["LDI"]: #RI
                    databin1 += registers[split[1]]
                    databin1 += "00"
                    databin2 = format(int(split[2]), "08b")
                elif split[0] in ["JMP", "JNZ", "JNN"]: #I
                    databin1 += "000"
                    H, L = splitStr(format(int(split[1]), "09b"), 1, 8)
                    databin1 += H
                    databin2 = L
                elif split[0] in ["MOV", "ADD", "SUB", "NND", "NOR"]: #RR
                    databin1 += registers[split[1]]
                    databin1 += registers[split[2]]

                data += str(int(databin1, 2)) + " "

            if split[0] in ["LDA", "STR", "LDI", "JMP", "JNZ", "JNN"]:
                data += str(int(databin2, 2)) + " "

    with open(outputname, "w") as file:
        file.write(data)