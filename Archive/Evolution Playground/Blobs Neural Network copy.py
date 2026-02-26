import numpy as np

def array2D(x, y):
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(0)

    return array

bodies = []
bodyNum = 2

class Body():
    def __init__(self, brain):
        self.brain = brain

    def think(self, inputs):
        for i in range(len(self.brain)):
            if i == 0:
                self.brain[i].forward(inputs)
                self.brain[i].activation()
            elif i == len(self.brain)-1:
                self.brain[i].forward(self.brain[i-1].nodeArray)
                self.brain[i].activation(output=True)
            else:
                self.brain[i].forward(self.brain[i-1].nodeArray)
                self.brain[i].activation()

        self.outputs = self.brain[len(self.brain)-1].nodeArray

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

    def activation(self, output=False):
        if output:
            self.nodeArray = [np.tanh(node) for node in self.nodeArray]
        else:
            self.nodeArray = [max(0, node) for node in self.nodeArray]

def create_brain(networkShape):
    layers = []
    for i in range(len(networkShape)-1):
        layers.append(Layer(networkShape[i], networkShape[i+1]))

    return layers

def main():
    inputs = [1,1]

    for i in range(bodyNum):
        bodies.append(Body(create_brain([2,4,4,2])))

    for body in bodies:
        body.think(inputs)

        print("Hidden 1:")
        print(body.brain[0].nodeArray)
        print(body.brain[0].weightsArray)
        print(body.brain[0].biasesArray)
        print("Hidden 2:")
        print(body.brain[1].nodeArray)
        print(body.brain[1].weightsArray)
        print(body.brain[1].biasesArray)
        print("Output Layer:")
        print(body.brain[2].nodeArray)
        print(body.brain[2].weightsArray)
        print(body.brain[2].biasesArray)
        print("Outputs:")
        print(body.outputs)
        print()

if __name__ == "__main__":
    main()