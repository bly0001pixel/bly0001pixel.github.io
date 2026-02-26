import pygame as py
from pygame import Vector2 as v2

FPS, WIDTH, HEIGHT = 60, 900, 77

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
road_marking_col = (200,200,50)

borderWidth = 3
CMWidth = 3
CMLength = 12
CMGap = 8

carWidth = 20
carLength = 40
carGap = 7
carCol = WHITE
carLane1 = v2(0, borderWidth+carGap)
carLane2 = v2(WIDTH-carLength, (HEIGHT/2)+(borderWidth/2)+carGap)

car_list = [
    [carLane1, v2(carLength, carWidth), v2(0,0), carCol, v2(0.01,0), v2(2,2)],
    [carLane2, v2(carLength, carWidth), v2(0,0), carCol, v2(-0.01,0), v2(2,2)]
]