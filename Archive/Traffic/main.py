import pygame as py
from settings import *
from vehicle import create_vehicles

py.init()
window = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Template")

def create_road_markings():
    road_markings = []

    #Top and bottom borders
    road_markings.append(((0,0), (WIDTH, borderWidth)))
    road_markings.append(((0, HEIGHT-borderWidth), (WIDTH, borderWidth)))

    #Center dash marking
    for i in range(int((WIDTH-CMGap)/(CMLength+CMGap))+1):
        road_markings.append(((CMGap+i*(CMLength+CMGap), HEIGHT/2-CMWidth/2), (CMLength, CMWidth)))

    return road_markings

def readout(vehicles):
    for vehicle in vehicles:
        print(vehicle.vel)
    print("\n")

def tick(vehicles):
    for vehicle in vehicles:
        vehicle.tick()

def draw_display(road_markings, vehicles):
    window.fill(BLACK)

    #Draw road markings
    for rect in road_markings:
        py.draw.rect(window, road_marking_col, rect)

    #Draw cars
    for vehicle in vehicles:
        py.draw.rect(window, vehicle.col, vehicle.rect)

def main():
    run = True
    clock = py.time.Clock()

    road_markings = create_road_markings()
    vehicles = create_vehicles()

    while run:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            elif event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                run = False

        tick(vehicles)
        readout(vehicles)

        draw_display(road_markings, vehicles)
        py.display.flip()

    py.quit()

if __name__ == "__main__":
    main()