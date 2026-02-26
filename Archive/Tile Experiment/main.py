import pygame
import math
import random
pygame.init()
pygame.font.init()
pygame.mixer.init()

HEIGHT = 500
WIDTH = 500
TILESIZE = 100
WORLD_TILE_WIDTH = 100
WORLD_TILE_HEIGHT = 100

MIDDLE_TILE_X = int((WORLD_TILE_WIDTH/2)-2.5)
MIDDLE_TILE_Y = int((WORLD_TILE_HEIGHT/2)-2.5)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tile Game")

FPS = 60

startingOffsetX = WIDTH/2-50
startingOffsetY = HEIGHT/2-50

tileData = {}

class Character:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (startingOffsetX,startingOffsetY)
        self.deltaX = 0
        self.deltaY = 0

class Grass:
    def __init__(self, image_path):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()

class Water:
    def __init__(self, image_path):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()

def read_nested_file(filename):
    gridDict = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(':')
                if len(parts) == 3:
                    cell_id, key, value = parts
                    if cell_id not in gridDict:
                        gridDict[cell_id] = {}
                    gridDict[cell_id][key] = value
    return gridDict

def procedural_generation(filename, WORLD_WIDTH, WORLD_HEIGHT):
    xCounter = 0
    yCounter = 0
    with open(filename, 'w') as file:
        for i in range(WORLD_HEIGHT):
            for i in range(WORLD_WIDTH):
                unknown = int(random.randint(1,6))
                if unknown < 6:
                    totalWrite1 = str(int(xCounter/100)+1) + "/" + str(int(yCounter/100)+1) + ":t:1"
                    totalWrite2 = str(int(xCounter/100)+1) + "/" + str(int(yCounter/100)+1) + ":x:" + str(xCounter)
                    totalWrite3 = str(int(xCounter/100)+1) + "/" + str(int(yCounter/100)+1) + ":y:" + str(yCounter)
                    file.write(totalWrite1 + '\n' + totalWrite2 + '\n' + totalWrite3 + '\n')
                elif unknown == 6:
                    totalWrite1 = str(int(xCounter/100)+1) + "/" + str(int(yCounter/100)+1) + ":t:2"
                    totalWrite2 = str(int(xCounter/100)+1) + "/" + str(int(yCounter/100)+1) + ":x:" + str(xCounter)
                    totalWrite3 = str(int(xCounter/100)+1) + "/" + str(int(yCounter/100)+1) + ":y:" + str(yCounter)
                    file.write(totalWrite1 + '\n' + totalWrite2 + '\n' + totalWrite3 + '\n')
                xCounter += 100
            xCounter = 0
            yCounter += 100

def process_cell_data(cell_id, attributes, character, grass, water):
    t_value = attributes.get('t')
    x_value = int(attributes.get('x'))
    y_value = int(attributes.get('y'))

    x_value += character.deltaX
    y_value += character.deltaY

    if t_value == "1":
        classID = grass.image
    elif t_value == "2": 
        classID = water.image

    return classID, x_value, y_value

def handle_movement(event, character, tileData):
    new_deltaX = character.deltaX
    new_deltaY = character.deltaY

    if event.key == pygame.K_w:
        new_deltaY += 100
    if event.key == pygame.K_a:
        new_deltaX += 100
    if event.key == pygame.K_s:
        new_deltaY -= 100
    if event.key == pygame.K_d:
        new_deltaX -= 100

    new_x_tile = (character.rect.topleft[0] + new_deltaX) // TILESIZE
    new_y_tile = (character.rect.topleft[1] + new_deltaY) // TILESIZE

    character.deltaX = new_deltaX
    character.deltaY = new_deltaY

def draw_display(tileData, character, grass, water):
    window.fill((255,255,255))

    for cell_id, attributes in tileData.items():
        classID, x_value, y_value = process_cell_data(cell_id, attributes, character, grass, water)
        window.blit(classID, (x_value, y_value))

    window.blit(character.image, character.rect.topleft)

    pygame.display.flip()

def main():
    clock = pygame.time.Clock() 

    procedural_generation('tileData.txt', WORLD_TILE_WIDTH, WORLD_TILE_HEIGHT)

    global tileData
    tileData = read_nested_file('tileData.txt')

    character = Character(image_path='MainCharacter.png')
    grass = Grass(image_path='Grass.png')
    water = Water(image_path='Water.png')

    character.deltaX = MIDDLE_TILE_X*-100
    character.deltaY = MIDDLE_TILE_Y*-100

    run = True
    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            if event.type == pygame.KEYDOWN:
                handle_movement(event, character, tileData)

        draw_display(tileData, character, grass, water)

    pygame.quit()

if __name__ == "__main__":
    main()