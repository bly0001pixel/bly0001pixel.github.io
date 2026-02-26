import pygame as py
from pygame import Vector2 as v2
py.init()

import random

FPS, WIDTH, HEIGHT = 60, 1400, 1200
window = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Pygame")

BLACK = (0,0,0)

tileSize = 40

class EndZone():
    def __init__(self):
        self.rect = py.rect.Rect(WIDTH-tileSize, 0, tileSize, HEIGHT)
        self.rect2 = py.rect.Rect(0, 0, tileSize, HEIGHT)
        self.colour = (150,150,150)

class RedPlayer():
    def __init__(self):
        self.pos = v2(0,0)
        self.size = v2(tileSize,tileSize)
        self.moveSpeed = v2(tileSize,tileSize)
        self.rect = py.rect.Rect(self.pos, self.size)
        self.normalColour = (255,0,0)
        self.invertedColour = (224, 127, 127)
        self.colour = self.normalColour

        self.movesDic = {
            "w":[v2(0,-1),v2(0,1)],
            "a":[v2(-1,0),v2(1,0)],
            "s":[v2(0,1),v2(0,-1)],
            "d":[v2(1,0),v2(-1,0)],
        }
        self.pastMoves = []

    def move(self, move):
        self.colour = self.normalColour

        if move in self.movesDic:
            newPos = v2(self.pos.x + self.movesDic[move][0].x * self.moveSpeed.x, self.pos.y + self.movesDic[move][0].y * self.moveSpeed.y)
            if newPos.x >= 0 and newPos.x < WIDTH and newPos.y >= 0 and newPos.y < HEIGHT/2:
                self.pos = newPos
                self.rect = py.rect.Rect(self.pos, self.size)
                self.pastMoves.insert(0, move)
                return True
            else:
                return False

    def invertedMove(self, index):
        self.colour = self.invertedColour

        if index >= len(self.pastMoves):
            return

        move = self.pastMoves[index]

        if move in self.movesDic:
            self.pos.x += self.movesDic[move][1].x * self.moveSpeed.x
            self.pos.y += self.movesDic[move][1].y * self.moveSpeed.y

        self.rect = py.rect.Rect(self.pos, self.size)        

class BluePlayer():
    def __init__(self):
        self.pos = v2(WIDTH-tileSize,HEIGHT/2)
        self.size = v2(tileSize,tileSize)
        self.moveSpeed = v2(tileSize,tileSize)
        self.rect = py.rect.Rect(self.pos, self.size)
        self.normalColour = (0,0,255)
        self.invertedColour = (102, 156, 237)
        self.colour = self.normalColour

        self.movesDic = {
            "w":[v2(0,-1),v2(0,1)],
            "a":[v2(-1,0),v2(1,0)],
            "s":[v2(0,1),v2(0,-1)],
            "d":[v2(1,0),v2(-1,0)],
        }
        self.pastMoves = []

    def move(self, move):
        self.colour = self.normalColour

        if move in self.movesDic:
            newPos = v2(self.pos.x + self.movesDic[move][0].x * self.moveSpeed.x, self.pos.y + self.movesDic[move][0].y * self.moveSpeed.y)
            if newPos.x >= 0 and newPos.x < WIDTH and newPos.y >= HEIGHT/2 and newPos.y < HEIGHT:
                self.pos = newPos
                self.rect = py.rect.Rect(self.pos, self.size)
                self.pastMoves.insert(0, move)
                return True
            else:
                return False

    def invertedMove(self, index):
        self.colour = self.invertedColour

        if index >= len(self.pastMoves):
            return

        move = self.pastMoves[index]

        if move in self.movesDic:
            self.pos.x += self.movesDic[move][1].x * self.moveSpeed.x
            self.pos.y += self.movesDic[move][1].y * self.moveSpeed.y

        self.rect = py.rect.Rect(self.pos, self.size)

gates = []

class Gate():
    def __init__(self, pos, side):
        self.pos = pos 
        self.side = side
        self.open = False

    def check(self, redPlayer, bluePlayer):
        if self.side == 0 and redPlayer.pos == self.pos:
            self.side = "xxx"
        elif self.side == 1 and bluePlayer.pos == self.pos:
            self.side = "xxx"

def create_gate():
    redPos = v2(random.randint(3, WIDTH/tileSize-4)*tileSize, random.randint(0, HEIGHT/tileSize/2)*tileSize)
    bluePos = v2()
    gate = Gate(redPos)

def move(redPlayer, bluePlayer, move, inverted, start, index):
    if start:
        redPlayer.move(move)
    else:
        if not inverted:
            if redPlayer.move(move):
                if index < len(bluePlayer.pastMoves):
                    bluePlayer.invertedMove(index)

        if inverted:
            bluePlayer.move(move)
            if index < len(redPlayer.pastMoves):
                redPlayer.invertedMove(index)

    print(f"RED: {redPlayer.pos}")
    print(f"BLUE: {bluePlayer.pos}")

def draw_display(redPlayer, bluePlayer, endZone, start, borderColour):
    window.fill(BLACK)

    py.draw.rect(window, endZone.colour, endZone.rect)
    py.draw.rect(window, endZone.colour, endZone.rect2)

    py.draw.rect(window, redPlayer.colour, redPlayer.rect)
    if not start or inverted:
        py.draw.rect(window, bluePlayer.colour, bluePlayer.rect)

    py.draw.rect(window, borderColour, (0, HEIGHT/2-3, WIDTH, 6))

def main():
    run = True
    clock = py.time.Clock()

    redPlayer = RedPlayer()
    bluePlayer = BluePlayer()
    endZone = EndZone()

    global inverted, index, start

    inverted = False
    index = 0
    start = True

    while run:
        clock.tick(FPS)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            elif event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                run = False

            if event.type == py.KEYDOWN and event.key == py.K_w:
                move(redPlayer, bluePlayer, "w", inverted, start, index)
                index += 1
            if event.type == py.KEYDOWN and event.key == py.K_a:
                move(redPlayer, bluePlayer, "a", inverted, start, index)
                index += 1
            if event.type == py.KEYDOWN and event.key == py.K_s:
                move(redPlayer, bluePlayer, "s", inverted, start, index)
                index += 1
            if event.type == py.KEYDOWN and event.key == py.K_d:
                move(redPlayer, bluePlayer, "d", inverted, start, index)
                index += 1

        if not inverted and redPlayer.pos.x >= WIDTH-tileSize-1 or inverted and bluePlayer.pos.x < tileSize:
            if start:
                start = False
            if inverted:
                inverted = False
                redPlayer.pos.x = 0
                redPlayer.pos.y = HEIGHT/2 - (bluePlayer.pos.y - (HEIGHT/2)) - tileSize
                redPlayer.rect = py.rect.Rect(redPlayer.pos, redPlayer.size)
                redPlayer.colour = redPlayer.normalColour
                bluePlayer.colour = bluePlayer.invertedColour
            else:
                inverted = True
                bluePlayer.pos.x = WIDTH-tileSize
                bluePlayer.pos.y = HEIGHT - redPlayer.pos.y - tileSize
                bluePlayer.rect = py.rect.Rect(bluePlayer.pos, bluePlayer.size)
                redPlayer.colour = redPlayer.invertedColour
                bluePlayer.colour = bluePlayer.normalColour
            index = 0
            print("invert")

        if inverted:
            borderColour = (0,0,255)
        else:
            borderColour = (255,0,0)

        draw_display(redPlayer, bluePlayer, endZone, start, borderColour)
        py.display.flip()

    py.quit()

if __name__ == "__main__":
    main()