import numpy as np
import tkinter as tk

root = tk.Tk()
root.title("AI")
root.geometry("400x400")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

infile = "train.txt"

def read_database(infile):
    inputs = []
    targets = []
    with open(infile, "r") as f:
        split = f.read().split(";")
        for line in split:
            if line.strip() != "":
                inputsS, targetsS = line.split("/")
                inputsL = [float(inputsS.split(",")[i]) for i in range(len(inputsS.split(",")))]
                targetsL = [float(targetsS.split(",")[i]) for i in range(len(targetsS.split(",")))]
                inputs.append(inputsL)
                targets.append(targetsL)

    database = list(zip(inputs, targets))

    return inputs, database

inputs, database = read_database(infile)

def show_frame(frame):
    frame.tkraise()

def activation(x):
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))

def activation_d(x):
    x = np.clip(x, -500, 500)
    s = 1 / (1 + np.exp(-x))
    return s * (1 - s)

class AI:
    def __init__(self, size):
        self.size = size
        self.weights = []
        self.biases = []
        self.layers = [np.zeros(n) for n in self.size]
        self.zvalues = [np.zeros(n) for n in self.size[1:]]
        for i in range(len(self.size)-1):
            weights_matrix = np.random.uniform(-0.5, 0.5, (self.size[i+1], self.size[i]))
            biases_matrix = np.random.uniform(-0.5, 0.5, self.size[i+1])
            self.weights.append(weights_matrix)
            self.biases.append(biases_matrix)
        self.weight_velocities = [np.zeros_like(w) for w in self.weights]
        self.bias_velocities = [np.zeros_like(b) for b in self.biases]

    def forward_pass(self, input, target):
        self.layers[0] = np.array(input)
        for i in range(len(self.size)-1):
            zvalue = np.dot(self.weights[i], self.layers[i]) + self.biases[i]
            self.zvalues[i] = zvalue
            self.layers[i+1] = activation(zvalue)
        self.cost = 0.5 * np.sum((self.layers[-1] - target) ** 2)
        return self.cost

    def backward_pass(self, target, learningRate, momentum):
        deltas = [np.zeros(n) for n in self.size[1:]]
        deltas[-1] = (self.layers[-1] - target) * activation_d(self.zvalues[-1])

        for i in reversed(range(len(self.size) - 2)):
            deltas[i] = np.dot(self.weights[i+1].T, deltas[i+1]) * activation_d(self.zvalues[i])

        for i in range(len(self.weights)):
            grad_w = np.outer(deltas[i], self.layers[i])
            grad_b = deltas[i]

            self.weight_velocities[i] = momentum * self.weight_velocities[i] - learningRate * grad_w
            self.bias_velocities[i] = momentum * self.bias_velocities[i] - learningRate * grad_b

            self.weights[i] += self.weight_velocities[i]
            self.biases[i] += self.bias_velocities[i]

def escape():
    start(inputs, database, True)

def randomise(net, randomiseFactor):
    for i in range(len(net.weights)):
        net.weights[i] += np.random.normal(-randomiseFactor, randomiseFactor, size=net.weights[i].shape)
        net.biases[i] += np.random.normal(-randomiseFactor, randomiseFactor, size=net.biases[i].shape)

trainFrame = tk.Frame(root)
trainFrame.grid(row=0, column=0, sticky="nsew")
trainingLabel = tk.Label(trainFrame, text="Training in progress...")
epochLabel = tk.Label(trainFrame, text="Epoch = 0")
costLabel = tk.Label(trainFrame, text="Cost = 1")
randomiseButton = tk.Button(trainFrame, text="Randomise")
escapeButton = tk.Button(trainFrame, text="Reset")

trainingLabel.pack()
epochLabel.pack()
costLabel.pack()
randomiseButton.pack()
escapeButton.pack()

def train(inputs, database, size, learningRate, maxEpochs, targetCost, outfile, momentum):
    show_frame(trainFrame)
    root.update()

    net = AI(size)

    escapeButton.config(command=escape)
    randomiseButton.config(command=randomise(net, 1))

    for epoch in range(maxEpochs + 1):
        total_cost = 0
        for input, target in database:
            total_cost += net.forward_pass(input, target)
            net.backward_pass(target, learningRate, momentum)
        avg_cost = total_cost / len(inputs)

        epochLabel.config(text=f"Epoch = {epoch}")
        costLabel.config(text=f"Avg Cost = {avg_cost:.10f}")

        root.update()

        if avg_cost < targetCost:
            break

    with open(outfile, "w") as f:
        f.write("Weights:\n" + str(net.weights))
        f.write("\nBiases:\n" + str(net.biases))

    trainingLabel.config(text="Training complete!")
    epochLabel.config(text=f"Epoch = {epoch}")
    costLabel.config(text=f"Final Cost = {avg_cost}")

    root.update()

def start(inputs, database, default):
    startFrame = tk.Frame(root)
    startFrame.grid(row=0, column=0, sticky="nsew")

    def clicked():
        sizeStr = str(sizeInputVar.get()).split(",")
        size = [int(s.strip()) for s in sizeStr]
        learningRate = float(LRInputVar.get())
        maxEpochs = int(MEInputVar.get())
        targetCost = float(TCInputVar.get())
        momentum = float(MOInputVar.get())
        outfile = str(OFInputVar.get())
        train(inputs, database, size, learningRate, maxEpochs, targetCost, outfile, momentum)

    def default_values():
        with open("defaultValues.txt", "r") as f:
            lineSplit = f.read().split(";\n")
            lineEnds = []
            for i in range(len(lineSplit)):
                line = lineSplit[i]
                split = line.split(":")
                lineEnds.append(split[1])
            sizeInputVar.set(lineEnds[0])
            LRInputVar.set(lineEnds[1])
            MEInputVar.set(lineEnds[2])
            TCInputVar.set(lineEnds[3])
            MOInputVar.set(lineEnds[4])
            OFInputVar.set(lineEnds[5])

    def save_default_values():
        with open("defaultValues.txt", "w") as f:
            f.write(f"size:{sizeInputVar.get()};\n")
            f.write(f"learningRate:{LRInputVar.get()};\n")
            f.write(f"maxEpochs:{MEInputVar.get()};\n")
            f.write(f"targetCost:{TCInputVar.get()};\n")
            f.write(f"momentum,:{MOInputVar.get()};\n")
            f.write(f"outputFile:{OFInputVar.get()}")

    sizeInputLabel = tk.Label(startFrame, text="Size")
    sizeInputVar = tk.StringVar()
    sizeInput = tk.Entry(startFrame, textvariable=sizeInputVar)

    LRInputLabel = tk.Label(startFrame, text="Learning Rate")
    LRInputVar = tk.StringVar()
    LRInput = tk.Entry(startFrame, textvariable=LRInputVar)

    MEInputLabel = tk.Label(startFrame, text="Max Epochs")
    MEInputVar = tk.StringVar()
    MEInput = tk.Entry(startFrame, textvariable=MEInputVar)

    TCInputLabel = tk.Label(startFrame, text="Target Cost")
    TCInputVar = tk.StringVar()
    TCInput = tk.Entry(startFrame, textvariable=TCInputVar)

    MOInputLabel = tk.Label(startFrame, text="Momentum")
    MOInputVar = tk.StringVar()
    MOInput = tk.Entry(startFrame, textvariable=MOInputVar)

    OFInputLabel = tk.Label(startFrame, text="Output File")
    OFInputVar = tk.StringVar()
    OFInput = tk.Entry(startFrame, textvariable=OFInputVar)

    defaultButton = tk.Button(startFrame, text="Insert Default", command=default_values)
    saveDefaultButton = tk.Button(startFrame, text="Save Default", command=save_default_values)
    startTrainingButton = tk.Button(startFrame, text="Start Training", command=clicked)

    sizeInputLabel.grid(row=0, column=0, sticky="w")
    sizeInput.grid(row=0, column=1)

    LRInputLabel.grid(row=1, column=0, sticky="w")
    LRInput.grid(row=1, column=1)

    MEInputLabel.grid(row=2, column=0, sticky="w")
    MEInput.grid(row=2, column=1)

    TCInputLabel.grid(row=3, column=0, sticky="w")
    TCInput.grid(row=3, column=1)

    MOInputLabel.grid(row=4, column=0, sticky="w")
    MOInput.grid(row=4, column=1)

    OFInputLabel.grid(row=5, column=0, sticky="w")
    OFInput.grid(row=5, column=1)

    defaultButton.grid(row=6, column=0, columnspan=2, pady=(10,0))
    saveDefaultButton.grid(row=7, column=0, columnspan=2)
    startTrainingButton.grid(row=8, column=0, columnspan=2)

    if default:
        default_values()

    show_frame(startFrame)

start(inputs, database, False)
tk.mainloop()