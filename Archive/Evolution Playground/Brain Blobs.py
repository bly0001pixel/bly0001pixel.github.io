import pygame
import random
import copy
import numpy as np
pygame.init()

FPS, WIDTH, HEIGHT = 60, 900, 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
ORANGE = (255, 165, 0)
RED = (255,0,0)
FOODCOLOUR = (0,255,0)

blobs = []
blobStartNum = 50
blobSize = 8
blobColours = [WHITE, YELLOW, ORANGE, RED]

foods = []
foodTimers = []
newFoodTimers = []
foodStartNum = 200
foodSize = 6
foodResetTime = 400

foodContent = 20

networkShape = [2,32,2]

'''
Inputs:
    0. closestFood x
    1. closestFood y
Outputs:
    0. movement x 
    1. movement y
'''

'''
Genes:
    0. mutationAmount
    1. mutationChance
    2. speed
'''

def round2(number):
    return '{:.2f}'.format(number)

def array2D(x, y):
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(0)

    return array

class Layer():
    def __init__(self, nInputs, nNodes):
        self.nInputs = nInputs
        self.nNodes = nNodes

        self.weightsArray = np.random.uniform(-5, 5, (nNodes, nInputs))
        self.biasesArray = np.random.uniform(-5, 5, nNodes)
        self.nodeArray = [0] * self.nNodes

    def forward(self, inputs):
        self.inputsArray = inputs
        self.nodeArray = [0] * self.nNodes
        for i in range(self.nNodes):
            for j in range(self.nInputs):
                self.nodeArray[i] += self.weightsArray[i][j] * self.inputsArray[j]
            self.nodeArray[i] += self.biasesArray[i]

    def activation(self, output=False):
        if output:
            self.nodeArray = [np.tanh(node) for node in self.nodeArray]
        else:
            self.nodeArray = [max(0, node) for node in self.nodeArray]

class Blob():
    def __init__(self, position, brain, DNA):
        self.brain = brain
        self.DNA = DNA

        self.position = position
        self.velocity = pygame.Vector2(0,0)
        self.speed = self.DNA[2]

        self.hunger = 1000
        self.eaten = 0
        self.hungerLoss = 0.5
        self.eatenLimit = 3

        self.mutationAmount = self.DNA[0]
        self.mutationChance = self.DNA[1]

    def findClosestFood(self):
        closestDistance = 999999

        for food in foods:
            distance = self.position.distance_to(food.position)

            if distance < blobSize:
                foods.remove(food)
                foodTimers.append(0)

                self.hunger += foodContent
                self.eaten += 1
                self.hunger = min(100, self.hunger)

            elif distance < closestDistance:
                closestDistance = distance
                self.closestFoodVector = food.position - self.position

    def think(self):
        inputs = [self.closestFoodVector.x, self.closestFoodVector.y]

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

    def move(self):
        self.velocity = pygame.Vector2(self.outputs[0], self.outputs[1])

        if self.velocity.length() > 0:
            self.velocity = self.velocity.normalize() * self.speed

        self.position += self.velocity

        if self.position.x <= 0 or self.position.x >= WIDTH - blobSize:
            self.velocity.x *= -1
            self.position.x = max(blobSize, min(self.position.x, WIDTH - blobSize))
        
        if self.position.x <= 0:
            self.position.x = blobSize
        elif self.position.x >= WIDTH - blobSize:
            self.position.x = WIDTH - blobSize

        if self.position.y <= 0 or self.position.y >= HEIGHT - blobSize:
            self.velocity.y *= -1
            self.position.y = max(blobSize, min(self.position.y, HEIGHT - blobSize))

        if self.position.y <= 0:
            self.position.y = blobSize
        elif self.position.y >= HEIGHT - blobSize:
            self.position.y = HEIGHT - blobSize

    def tick(self):
        self.hunger -= self.hungerLoss
        if self.hunger <= 0:
            blobs.remove(self)
            return
        
        if self.eaten >= self.eatenLimit:
            self.eaten = 0
            create_blob(False, self.position, self.brain, self.DNA, self.mutationAmount, self.mutationChance)

        self.findClosestFood()

        self.think()
        self.move()

class Food():
    def __init__(self, position):
        self.position = position

def create_brain():
    layers = []
    for i in range(len(networkShape)-1):
        layers.append(Layer(networkShape[i], networkShape[i+1]))

    return layers

def mutate_brain(oldBrain, mutationAmount, mutationChance):
    newBrain = copy.deepcopy(oldBrain)

    for layer in newBrain:
        for i in range(len(layer.weightsArray)):
            for j in range(len(layer.weightsArray[i])):
                if random.uniform(0, 1) < mutationChance:
                    layer.weightsArray[i][j] += random.uniform(-mutationAmount, mutationAmount)
        for i in range(len(layer.biasesArray)):
            if random.uniform(0, 1) < mutationChance:
                layer.biasesArray[i] += random.uniform(-mutationAmount, mutationAmount)
    
    return newBrain

def mutate_DNA(oldDNA, mutationAmount, mutationChance):
    newDNA = copy.deepcopy(oldDNA)

    if random.uniform(0, 1) < mutationChance:
        newDNA[0] += random.uniform(-mutationAmount, mutationAmount) / 100
    if random.uniform(0, 1) < mutationChance:
        newDNA[1] += random.uniform(-mutationAmount, mutationAmount) / 100
    if random.uniform(0, 1) < mutationChance:
        newDNA[2] += random.uniform(-mutationAmount, mutationAmount)

    return newDNA

def create_blob(start, position, oldBrain, oldDNA, mutationAmount, mutationChance):
    if start:
        speed = random.uniform(0, 1)
        mutationAmount = random.uniform(0.01, 0.1)
        mutationChance = random.uniform(0.01, 0.1)
        DNA = [
            mutationAmount,
            mutationChance,
            speed,
        ]

        blobs.append(Blob(position, create_brain(), DNA))

    else:
        blobs.append(Blob(position, mutate_brain(copy.deepcopy(oldBrain), mutationAmount, mutationChance), mutate_DNA(copy.deepcopy(oldDNA), mutationAmount, mutationChance)))

def create_food():
    position = pygame.Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT))

    foods.append(Food(position))

def start():
    for i in range(0, blobStartNum):
        create_blob(True, pygame.Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)), None, None, None, None)

    for i in range(0, foodStartNum):
        create_food()

def reset_food():
    global foodTimers
    newFoodTimers = []

    for timer in foodTimers:
        timer += 1
        if timer >= foodResetTime:
            create_food()
        else:
            newFoodTimers.append(timer)
        
    foodTimers = newFoodTimers

def draw_display():
    window.fill(BLACK)

    for blob in blobs:
        pygame.draw.circle(window, blobColours[blob.eaten], blob.position, blobSize)

    for food in foods:
        pygame.draw.rect(window, FOODCOLOUR, pygame.Rect(food.position.x - foodSize//2, food.position.y - foodSize//2, foodSize, foodSize))

def main():
    run = True
    clock = pygame.time.Clock()
    
    start()

    global foodTimers

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        reset_food()

        for blob in blobs:
            blob.tick()

        draw_display()
        pygame.display.flip()

        print(len(blobs))

    pygame.quit()

if __name__ == "__main__":
    main()