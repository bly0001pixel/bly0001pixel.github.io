import pygame
from pygame import Vector2 as v2
pygame.init()

import random
import math

FPS, WIDTH, HEIGHT = 60, 900, 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

gridWidth = 30
gridHeight = 30
cellWidth = WIDTH/gridWidth

def create_points():
    points = []
    centerPoints = []
    for i in range(gridWidth-1):
        row = []
        CProw = []
        for j in range(gridHeight-1):
            if i % 3 != j % 2:
                x = (i+1) * cellWidth if j % 2 == 0 else (i+1) * cellWidth + (cellWidth / 2)
                y = (j+1) * cellWidth * 0.85
                row.append(v2(x,y))
            else:
                x = (i+1) * cellWidth if j % 2 == 0 else (i+1) * cellWidth + (cellWidth / 2)
                y = (j+1) * cellWidth * 0.85
                CProw.append(v2(x,y))

        points.append(row)
        centerPoints.append(CProw)
        
    return points, centerPoints

def hexagon_edges(center, width=cellWidth*2):
    cx, cy = center.x, center.y
    r = width / 2.0  # radius from center to any vertex

    # Compute 6 vertices of the hexagon
    vertices = [
        (cx + r * math.cos(math.radians(angle)),
         cy + r * math.sin(math.radians(angle)))
        for angle in range(0, 360, 60)
    ]

    # Create list of edges (pairs of consecutive vertices)
    edges = [(vertices[i], vertices[(i + 1) % 6]) for i in range(6)]

    return edges

def create_edges(centerPoints):
    edges = []

    for row in centerPoints:
        for point in row:
            edges.append(hexagon_edges(point))

    return edges

points, centerPoints = create_points()
edges = create_edges(centerPoints)

def draw_display():
    window.fill(BLACK)

    for row in points:
        for point in row:
            pygame.draw.circle(window, WHITE, (point.x, point.y), cellWidth/7)

    #for row in centerPoints:
        #for point in row:
            #pygame.draw.circle(window, RED, (point.x, point.y), cellWidth/5)

    for cell in edges:
        for edge in cell:
            pygame.draw.line(window, WHITE, edge[0], edge[1])

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