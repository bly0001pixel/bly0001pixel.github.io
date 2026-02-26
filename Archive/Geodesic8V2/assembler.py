import os

script_dir = os.path.dirname(__file__)
inputname = os.path.join(script_dir, "input.txt")
outputname = os.path.join(script_dir, "output.txt")

opcodes = {
    "NOTH":"00000", #0
    "HALT":"00001", #0
    "LODA":"00010", #RA
    "LODI":"00011", #RI
    "STR":"00100", #RA
    "TRNW":"00110", #R
    "TRNR":"00111", #R
    "ALA+":"01000", #RA
    "ALA-":"01001", #RA
    "ALI+":"01010", #RI
    "ALI-":"01011", #RI
    "JMP":"01100", #I
    "JPZT":"01110", #I
    "JPZF":"01111", #I
    "JPNT":"10000", #I
    "JPNF":"10001", #I
    "AND":"10010", #RA
    "OR":"10100", #RA
    "AANB":"10110", #RA
    "AONB":"10111", #RA
    "NOT":"11000", #R
    "LSHL":"11010", #R
    "LSHR":"11011", #R
    "ASH":"11100", #R
    "UPD":"11110" #0
}

registers = {
    "A":"00",
    "B":"01",
    "C":"10",
    "ALU":"11"
}

data = "0 "

with open(inputname, "r") as file:
    for line in file:
        if line:
            databin = ""
            split = line.strip().split(" ")
            databin += opcodes[split[0]]
            if split[0] in ["NOTH", "HALT", "UPD"]:
                databin += "00000000000"
            elif split[0] in ["TRNW", "TRNR", "NOT", "LSHL", "LSHR", "ASH"]:
                databin += registers[split[1]]
                databin += "000000000"
            elif split[0] in ["LODA", "ALA+", "ALA-", "AND", "OR", "AANB", "AONB", "STR"]:
                databin += registers[split[1]]
                databin += format(int(split[2]), "09b")
            elif split[0] in ["LODI", "ALI+", "ALI-"]:
                databin += registers[split[1]]
                databin += "0"
                databin += format(int(split[2]), "08b")
            elif split[0] in ["JMP", "JPZT", "JPZF", "JPNT", "JPNF"]:
                databin += "000"
                databin += format(int(split[1]), "08b")

        data += str(int(databin, 2)) + " "
    data += "2048"

with open(outputname, "w") as file:
    file.write(data)