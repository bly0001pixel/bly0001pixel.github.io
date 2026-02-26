import pygame as py
from settings import car_list

class Vehicle:
    def __init__(self, pos, size, vel, col, acc, spdlmt):
        self.pos = pos
        self.size = size
        self.rect = py.Rect(self.pos, self.size)
        self.vel = vel
        self.col = col
        self.acc = acc
        self.spdlmt = spdlmt

    def tick(self):
        if abs(self.vel.x + self.acc.x) <= self.spdlmt.x:
            self.vel.x += self.acc.x
        if abs(self.vel.y + self.acc.y) <= self.spdlmt.y:
            self.vel.y += self.acc.y

        self.pos += self.vel
        self.rect = py.Rect(self.pos, self.size)

def create_vehicles():
    vehicles = []
    for i in range(len(car_list)):
        vehicle = Vehicle(
            car_list[i][0], car_list[i][1], car_list[i][2], 
            car_list[i][3], car_list[i][4], car_list[i][5])
        vehicles.append(vehicle)
    return vehicles