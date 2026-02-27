import pygame
from pygame import Vector2 as v2
pygame.init()

import random

FPS, WIDTH, HEIGHT = 60, 900, 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")

BLACK = (0,0,0)
WHITE = (255,255,255)

cellNum = 20
cellSize = WIDTH / cellNum

points = [[v2(i*cellSize + random.randint(int(cellSize/5),int(cellSize-(cellSize/5))), j*cellSize + random.randint(int(cellSize/5),int(cellSize-(cellSize/5)))) for i in range(int(cellNum))] for j in range(int(cellNum))]

for row in points:
    for point in row:
        for i in range(-1,2):
            for j in range(-1,2):
                

def draw_display():
    window.fill(BLACK)

    for row in points:
        for point in row:
            pygame.draw.circle(window, WHITE, (point.x, point.y), cellSize / 10)

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        draw_display()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()