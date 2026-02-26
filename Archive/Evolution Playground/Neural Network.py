import numpy as np

def array2D(x, y):
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(0)

    return array

def sig(x):
    return 1/(1 + np.exp(-x))

bodyNum = 1
networkShape = [2,2,1]
inputs = [0.35, 0.7]
outputGoal = [0.5]
learningRate = 1

bodies = []

class Body():
    def __init__(self, brain):
        self.brain = brain

    def think(self, inputs):
        for i in range(len(self.brain)):
            if i == 0:
                self.brain[i].forward(inputs)
                self.brain[i].activation("sigmoid")
            elif i == len(self.brain)-1:
                self.brain[i].forward(self.brain[i-1].nodeArray)
                self.brain[i].activation("sigmoid")
            else:
                self.brain[i].forward(self.brain[i-1].nodeArray)
                self.brain[i].activation("sigmoid")

        self.outputs = self.brain[len(self.brain)-1].nodeArray
    
    def error(self):
        self.outputError = 0.5 * ((outputGoal - self.output) * (outputGoal - self.output))

class Layer():
    def __init__(self, nInputs, nNodes):
        self.nInputs = nInputs
        self.nNodes = nNodes

        self.weightsArray = np.random.uniform(-1, 1, (nNodes, nInputs))
        self.biasesArray = np.random.uniform(-1, 1, nNodes)
        self.nodeArray = [0] * self.nNodes

    def forward(self, inputs):
        self.inputsArray = inputs
        for i in range(self.nNodes):
            for j in range(self.nInputs):
                self.nodeArray[i] += self.weightsArray[i][j] * self.inputsArray[j]
            self.nodeArray[i] += self.biasesArray[i]

    def activation(self, type):
        if type == "tanh":
            self.nodeArray = [np.tanh(node) for node in self.nodeArray]
        elif type == "sigmoid":
            self.nodeArray = [sig(node) for node in self.nodeArray]
        else:
            self.nodeArray = [max(0, node) for node in self.nodeArray]

def create_brain():
    layers = []
    for i in range(len(networkShape)-1):
        layers.append(Layer(networkShape[i], networkShape[i+1]))

    return layers

def main():
    for i in range(bodyNum):
        bodies.append(Body(create_brain()))

    for body in bodies: 
        body.think(inputs)
        body.error()

if __name__ == "__main__":
    main()