with open("train.csv", "r") as f:
    inputs = []
    targets = []
    for line in f.readlines():
        inputsS = ""
        targetsS = ""

        split = list(line.split(","))
        print(split)

        inputsS += split[0]  + ","
        targetsS += split[1]
        inputsS += split[2]  + ","
        #Ignore 3, Name
        #ignore 4, Name
        inputsS += str(0 if split[5] == "male" else 1)  + ","
        inputsS += split[6]  + ","
        inputsS += split[7]  + ","
        inputsS += split[8]  + ","
        #Ignore 9, ticket
        inputsS += split[10]
        #Ignore 11, cabin
        #Ignore 12, port

        inputs.append(inputsS)
        targets.append(targetsS)

with open("train.txt", "w") as l:
    for i in range(len(inputs)):
        l.write(inputs[i] + "/" + targets[i] + ";\n")