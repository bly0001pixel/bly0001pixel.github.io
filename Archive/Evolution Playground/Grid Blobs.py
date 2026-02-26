import pygame
import random
import os
import time
pygame.init()

FPS, WIDTH, HEIGHT = 60, 1000, 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")

BLACK = (0,0,0)

speed = 2

startNum = 2000
generationLength = 10000 / speed
pauseLength = 1000
mutationChance = 30
mutationDistanceMin = 1
mutationDistanceMax = 30
reproductionNum = 6
blobSize = 3

elimWallN1 = 0
elimWallE1 = 50
elimWallS1 = HEIGHT
elimWallW1 = -100

elimWallN2 = 0
elimWallE2 = WIDTH+100
elimWallS2 = HEIGHT
elimWallW2 = WIDTH-50

blobs = []

maxBlobs = 3000

class Blob():
    def __init__(self, position, mChance, mCD, colour):
        self.size = blobSize
        self.position = position
        self.mChance = mChance
        self.mCD = mCD
        self.colour = colour

    def move(self):
        if random.randint(0, 100) < self.mChance:
            raffle = []
            for i in range(len(self.mCD)):
                raffle.extend([i] * self.mCD[i])

            if raffle:
                rafflePick = random.choice(raffle)

                directions = [
                    pygame.Vector2(0, -1),   # North
                    pygame.Vector2(1, -1),   # Northeast
                    pygame.Vector2(1, 0),    # East
                    pygame.Vector2(1, 1),    # Southeast
                    pygame.Vector2(0, 1),    # South
                    pygame.Vector2(-1, 1),   # Southwest
                    pygame.Vector2(-1, 0),   # West
                    pygame.Vector2(-1, -1),  # Northwest
                ]

                newPosition = self.position + directions[rafflePick] * self.size * speed
                self.position.x = max(0, min(WIDTH - self.size, newPosition.x))
                self.position.y = max(0, min(HEIGHT - self.size, newPosition.y))

def start():
    for i in range(0, startNum):
        position = pygame.Vector2(random.randint(0, int(WIDTH/blobSize)) * blobSize, random.randint(0, int(HEIGHT/blobSize)) * blobSize)
        colour = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

        mChance = random.randint(0, 100)
        mNC = random.randint(0, 100)
        mNEC = random.randint(0, 100)
        mEC = random.randint(0, 100)
        mSEC = random.randint(0, 100)
        mSC = random.randint(0, 100)
        mSWC = random.randint(0, 100)
        mWC = random.randint(0, 100)
        mNWC = random.randint(0, 100)

        mCD = [
            mNC,
            mNEC,
            mEC,
            mSEC,
            mSC,
            mSWC,
            mWC,
            mNWC,
        ]

        blobs.append(Blob(position, mChance, mCD, colour))

def reproduce():
    global blobs
    newBlobs = []

    for oldBlob in blobs:
        for i in range(0, reproductionNum):
            if len(newBlobs) < maxBlobs:
                newPosition = pygame.Vector2(random.randint(0, int(WIDTH/blobSize)) * blobSize, random.randint(0, int(HEIGHT/blobSize)) * blobSize)

                mutationColourDistance = random.randint(mutationDistanceMin, mutationDistanceMax)
                oldColour = list(oldBlob.colour)
                newR = oldColour[0] + random.randint(-mutationColourDistance, mutationColourDistance)
                newG = oldColour[1] + random.randint(-mutationColourDistance, mutationColourDistance)
                newB = oldColour[2] + random.randint(-mutationColourDistance, mutationColourDistance)
                newColour = (min(255, max(50, newR)), min(255, max(50, newG)), min(255, max(50, newB)))

                newChance = oldBlob.mChance + random.randint(-mutationChance, mutationChance)
                newChance = min(100, max(0, newChance))
                
                newNC = oldBlob.mCD[0]
                newNEC = oldBlob.mCD[1]
                newEC = oldBlob.mCD[2]
                newSEC = oldBlob.mCD[3]
                newSC = oldBlob.mCD[4]
                newSWC = oldBlob.mCD[5]
                newWC = oldBlob.mCD[6]
                newNWC = oldBlob.mCD[7]

                mutationDistance = random.randint(mutationDistanceMin, mutationDistanceMax)
                if random.randint(0, 100) < mutationChance:
                    newNC += random.randint(-mutationDistance, mutationDistance)
                mutationDistance = random.randint(mutationDistanceMin, mutationDistanceMax)
                if random.randint(0, 100) < mutationChance:
                    newNEC += random.randint(-mutationDistance, mutationDistance)
                mutationDistance = random.randint(mutationDistanceMin, mutationDistanceMax)
                if random.randint(0, 100) < mutationChance:
                    newEC += random.randint(-mutationDistance, mutationDistance)
                mutationDistance = random.randint(mutationDistanceMin, mutationDistanceMax)
                if random.randint(0, 100) < mutationChance:
                    newSEC += random.randint(-mutationDistance, mutationDistance)
                mutationDistance = random.randint(mutationDistanceMin, mutationDistanceMax)
                if random.randint(0, 100) < mutationChance:
                    newSC += random.randint(-mutationDistance, mutationDistance)
                mutationDistance = random.randint(mutationDistanceMin, mutationDistanceMax)
                if random.randint(0, 100) < mutationChance:
                    newSWC += random.randint(-mutationDistance, mutationDistance)
                mutationDistance = random.randint(mutationDistanceMin, mutationDistanceMax)
                if random.randint(0, 100) < mutationChance:
                    newWC += random.randint(-mutationDistance, mutationDistance)
                mutationDistance = random.randint(mutationDistanceMin, mutationDistanceMax)
                if random.randint(0, 100) < mutationChance:
                    newNWC += random.randint(-mutationDistance, mutationDistance)
                mutationDistance = random.randint(mutationDistanceMin, mutationDistanceMax)

                newMCD = [
                    newNC, #North 0
                    newNEC, #North East 1
                    newEC, #East 2
                    newSEC, #South East 3
                    newSC, #South 4
                    newSWC, #South West 5
                    newWC, #West 6
                    newNWC, #North West 7
                ]
                
                newBlobs.append(Blob(newPosition, newChance, newMCD, newColour))

    blobs = newBlobs
    print(f"Num = {len(newBlobs)}")

def eliminate():
    global blobs
    #blobs = [blob for blob in blobs if elimWallW1 < blob.position.x < elimWallE1 and elimWallN1 < blob.position.y < elimWallS1]
    blobs = [blob for blob in blobs if elimWallW1 < blob.position.x < elimWallE1 and elimWallN1 < blob.position.y < elimWallS1 or elimWallW2 < blob.position.x < elimWallE2 and elimWallN2 < blob.position.y < elimWallS2]
    print(f"Survived = {len(blobs)}")

def draw_display(paused):
    window.fill(BLACK)

    for blob in blobs:
        if not paused:
            blob.move()
        else:
            pygame.draw.rect(window, (255,0,0), (elimWallW1,elimWallN1, elimWallE1-elimWallW1,elimWallS1-elimWallN1), 3)
            pygame.draw.rect(window, (255,0,0), (elimWallW2,elimWallN2, elimWallE2-elimWallW2,elimWallS2-elimWallN2), 3)
        pygame.draw.circle(window, blob.colour, blob.position, blob.size)

def main():
    run = True
    clock = pygame.time.Clock()
    
    start()

    startTime = pygame.time.get_ticks()
    generation = 0

    paused = False
    generationStartTime = startTime
    pauseStartTime = 0

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        currentTime = pygame.time.get_ticks()

        if not paused:
            if currentTime - generationStartTime >= generationLength:
                eliminate()
                paused = True
                pauseStartTime = currentTime

        else:
            if currentTime - pauseStartTime >= pauseLength:
                reproduce()
                generationStartTime = currentTime
                generation += 1
                paused = False

        draw_display(paused)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()