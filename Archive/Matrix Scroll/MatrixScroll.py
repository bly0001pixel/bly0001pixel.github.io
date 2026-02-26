import pygame
import random
pygame.init()
pygame.font.init()

FPS = 60

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Matrix Scroll")

WIDTH = window.get_width()
HEIGHT = window.get_height()

characterFont = pygame.font.Font("NotoSansJP-VariableFont_wght.ttf", 15)

BLACK = (0,0,0)

charactersList = [
    "ア", "イ", "ウ", "エ", "オ",
    "カ", "キ", "ク", "ケ", "コ",
    "サ", "シ", "ス", "セ", "ソ",
    "タ", "チ", "ツ", "テ", "ト",
    "ナ", "ニ", "ヌ", "ネ", "ノ",
    "ハ", "ヒ", "フ", "ヘ", "ホ",
    "マ", "ミ", "ム", "メ", "モ",
    "ヤ", "ユ", "ヨ",
    "ラ", "リ", "ル", "レ", "ロ",
    "ワ", "ヲ",
    "ン", 
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

characterColours = [
    (0, 255, 0),
]

characterColumns = []

columnWidth = 20
speed = 3
fadeSpeed = 4
colourSpeed = 500
colourSwitchLimit = 360

class Character: 
    def __init__(self, x, y, colour):
        self.position = pygame.Vector2(x, y)
        self.colourIndex = random.randint(0, len(characterColours)-1)
        self.colour = characterColours[self.colourIndex]
        self.darkColour = self.colour
        self.character = charactersList[random.randint(0,len(charactersList)-1)]
        self.timer = 0
        self.textRender = characterFont.render(self.character, 1, self.darkColour)

    def darken(self):
        darkR = max(0, self.colour[0] - self.timer)
        darkG = max(0, self.colour[1] - self.timer)
        darkB = max(0, self.colour[2] - self.timer)

        self.darkColour = (darkR, darkG, darkB)
        self.textRender = characterFont.render(self.character, 1, self.darkColour)
        self.timer += fadeSpeed
        return darkR, darkG, darkB
    

def draw_display():
    window.fill(BLACK)

    for column in characterColumns:
        for character in column:
            window.blit(character.textRender, character.position)

def main():
    clock = pygame.time.Clock()
    run = True
    timer = 0
    colourSwitchCounter = 0

    allColourIndex = random.randint(0, len(characterColours)-1)
    allColour = characterColours[allColourIndex]

    for i in range(0, WIDTH, columnWidth):
        characterColumns.append([])
    for x, column in enumerate(characterColumns):
        character = Character(x*columnWidth, random.randint(-int(HEIGHT), 0), allColour)
        column.append(character)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        timer += 1

        if timer >= speed:
            for x, column in enumerate(characterColumns):
                newX = x * columnWidth
                newY = column[-1].position.y + column[-1].textRender.get_height() - 4
                if newY > HEIGHT:
                    newY = random.randint(-10, 0)
                character = Character(newX, newY, allColour)
                column.append(character)

            timer = 0

            colourSwitchCounter += 1
            if colourSwitchCounter >= colourSwitchLimit:
                allColourIndex = (allColourIndex + 1) % len(characterColours)
                allColour = characterColours[allColourIndex]
                colourSwitchCounter = 0

        for column in characterColumns:
            for character in column:
                darkR, darkG, darkB = character.darken()
                if darkR == 0 and darkG == 0 and darkB == 0:
                    column.remove(character)

        draw_display()

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()