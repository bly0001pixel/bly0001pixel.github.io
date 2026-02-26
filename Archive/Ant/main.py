import pygame
import random
import math
pygame.init()

FPS, WIDTH, HEIGHT = 5, 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ant Simulator")

BLACK = (0,0,0)
GREY = (50,50,50)
RED = (255,20,20)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

tileSize = pygame.Vector2(5,5)

startColonyList = [[pygame.Vector2(60,60)]]
colonySize = 3

startFoodlist = [pygame.Vector2(60,10), pygame.Vector2(60,110), pygame.Vector2(10,60), pygame.Vector2(110,60)]

antStartNum = 200
antTurnChance = 7

pheremoneTimer = 3000
pheremoneDecay = 0.95

colonies = []
foods = []
pheremones = []
ants = []

class Colony:
    def __init__(self, tile):
        self.tile = tile
        self.displayTile = tile-pygame.Vector2(round(colonySize/2,0),round(colonySize/2,0))
        self.rect = (self.displayTile.x*tileSize.x, self.displayTile.y*tileSize.y, tileSize.x*colonySize, tileSize.y*colonySize)

class Food:
    def __init__(self, tile):
        self.tile = tile
        self.rect = pygame.Rect(self.tile.x*tileSize.x, self.tile.y*tileSize.y, tileSize.x, tileSize.y)

class Pheremone:
    def __init__(self, tile, type):
        self.tile = tile
        self.type = type
        self.timer = pheremoneTimer
        self.strength = self.timer/pheremoneTimer
        self.colour = (0,255*self.strength,0)
        self.radius = self.strength*((tileSize.x + tileSize.y)/4)

    def tick(self):
        self.timer *= pheremoneDecay
        self.strength = self.timer/pheremoneTimer
        self.colour = (0,255*self.strength,0)

class Ant:
    def __init__(self, tile):
        self.tile = tile
        self.foodFound = False
        self.rect = pygame.Rect(self.tile.x*tileSize.x, self.tile.y*tileSize.y, tileSize.x, tileSize.y)
        self.colour = BLUE if self.foodFound else YELLOW
        self.velocity = pygame.Vector2(random.randint(-1,1), random.randint(-1,1))

    def tick(self):
        for food in foods:
            if food.tile == self.tile and not self.foodFound:
                self.foodFound = True

        self.colour = BLUE if self.foodFound else YELLOW

        if not self.foodFound:
            strongest = 0
            strongestVector = self.velocity
            if len(pheremones) > 0:
                for pheremone in pheremones:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if pheremone.tile == pygame.Vector2(i,j) and pheremone.strength > strongest and pheremone.type == 0:
                                strongest = pheremone.strength
                                strongestVector = pygame.Vector2(i,j)
                self.velocity = strongestVector
            elif random.randint(1,antTurnChance) == 1:
                self.velocity = pygame.Vector2(random.randint(-1,1), (random.randint(-1,1)))
        else: 
            closest = WIDTH * HEIGHT
            closestVector = pygame.Vector2(0,0)
            for colony in colonies:
                distance = math.dist(self.tile, colony.tile)
                if distance < closest:
                    closest = distance
                    closestVector = colony.tile-self.tile

            if closest > 0:
                self.velocity = pygame.Vector2(int(round(closestVector.x/closest, 0)), int(round(closestVector.y/closest, 0)))
                pheremone = Pheremone(self.tile, 0)
                pheremones.append(pheremone)
            else:
                self.foodFound = False
                self.velocity = pygame.Vector2(random.randint(-1,1), (random.randint(-1,1)))
            
        newx = self.tile.x + self.velocity.x
        newy = self.tile.y + self.velocity.y
        if 0 <= newx < (WIDTH / tileSize.x) and 0 <= newy < (HEIGHT / tileSize.y):
            self.tile.x = newx
            self.tile.y = newy
        else:
            self.velocity *= -1
        self.rect = pygame.Rect(self.tile.x*tileSize.x, self.tile.y*tileSize.y, tileSize.x, tileSize.y)

def start():
    for i in range(len(startColonyList)):
        colony = Colony(startColonyList[i][0])
        colonies.append(colony)

    for i in range(antStartNum):
        ant = Ant(colonies[random.randint(0,len(colonies)-1)].tile+pygame.Vector2(random.randint(-2,0),random.randint(-2,0)))
        ants.append(ant)

    for tile in startFoodlist:
        food = Food(tile)
        foods.append(food)

def draw_display():
    window.fill(BLACK)

    for i in range(round(int(WIDTH/tileSize.x), 0)):
        pygame.draw.line(window, GREY, (i*tileSize.x, 0), (i*tileSize.x, HEIGHT))
    for i in range(round(int((HEIGHT/tileSize.y)), 0)):
        pygame.draw.line(window, GREY, (0, i*tileSize.y), (WIDTH, i*tileSize.y))

    for pheremone in pheremones:
        pygame.draw.circle(window, pheremone.colour, pygame.Vector2(pheremone.tile.x * tileSize.x + tileSize.x/2, pheremone.tile.y * tileSize.y + tileSize.y/2), pheremone.radius)

    for ant in ants:
        pygame.draw.rect(window, ant.colour, ant.rect)

    for colony in colonies:
        pygame.draw.rect(window, RED, colony.rect)

    for food in foods:
        pygame.draw.rect(window, GREEN, food.rect)

def main():
    run = True
    clock = pygame.time.Clock()

    start()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        for ant in ants:
            ant.tick()
            if 0 > ant.tile.x*tileSize.x > WIDTH or 0 > ant.tile.y*tileSize.y > HEIGHT:
                ants.remove(ant)
        for pheremone in pheremones:
            pheremone.tick()

        draw_display()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()