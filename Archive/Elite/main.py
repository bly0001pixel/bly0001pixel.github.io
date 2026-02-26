import pygame
from pygame import Vector2 as v2
from pygame import Vector3 as v3
pygame.init()

import math
from math import pi as pi

import os
script_dir = os.path.dirname(__file__)

FPS, WIDTH, HEIGHT = 60, 1500, 1500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Line")

BLACK = (0,0,0)
WHITE = (255,255,255)

lineWidth = 1
rotationSpeed = 0.1
moveSpeed = 0.1
depthFactor = 300

objects = []

def rotate_object(v3points, rotation, scale):
    centerOffset = v3(sum(p.x for p in v3points) / len(v3points), sum(p.y for p in v3points) / len(v3points), sum(p.z for p in v3points) / len(v3points))

    v3pointsR = []
    for points in v3points:
        p = v3(points.x, points.y, points.z)
        p -= centerOffset
        p *= scale

        v3pointsRx = v3()
        v3pointsRx.x = p.x
        v3pointsRx.y = (math.cos(rotation.x) * p.y) + (-1 * math.sin(rotation.x) * p.z)
        v3pointsRx.z = (math.sin(rotation.x) * p.y) + (math.cos(rotation.x) * p.z)

        v3pointsRy = v3()
        v3pointsRy.x = (math.cos(rotation.y) * v3pointsRx.x) + (math.sin(rotation.y) * v3pointsRx.z)
        v3pointsRy.y = v3pointsRx.y
        v3pointsRy.z = (-1 * math.sin(rotation.y) * v3pointsRx.x) + (math.cos(rotation.y) * v3pointsRx.z)

        v3pointsRz = v3()
        v3pointsRz.x = (math.cos(rotation.z) * v3pointsRy.x) + (-1 * math.sin(rotation.z) * v3pointsRy.y)
        v3pointsRz.y = (math.sin(rotation.z) * v3pointsRy.x) + (math.cos(rotation.z) * v3pointsRy.y)
        v3pointsRz.z = v3pointsRy.z

        p += centerOffset
        p /= scale
        v3pointsR.append(v3pointsRz)

    return v3pointsR

def rotate_normal(faceNormals, rotation):
    faceNormalsR = []
    for normal in faceNormals:
        faceNormalsRx = v3()
        faceNormalsRx.x = normal.x
        faceNormalsRx.y = (math.cos(rotation.x) * normal.y) + (-1 * math.sin(rotation.x) * normal.z)
        faceNormalsRx.z = (math.sin(rotation.x) * normal.y) + (math.cos(rotation.x) * normal.z)

        faceNormalsRy = v3()
        faceNormalsRy.x = (math.cos(rotation.y) * faceNormalsRx.x) + (math.sin(rotation.y) * faceNormalsRx.z)
        faceNormalsRy.y = faceNormalsRx.y
        faceNormalsRy.z = (-1 * math.sin(rotation.y) * faceNormalsRx.x) + (math.cos(rotation.y) * faceNormalsRx.z)

        faceNormalsRz = v3()
        faceNormalsRz.x = (math.cos(rotation.z) * faceNormalsRy.x) + (-1 * math.sin(rotation.z) * faceNormalsRy.y)
        faceNormalsRz.y = (math.sin(rotation.z) * faceNormalsRy.x) + (math.cos(rotation.z) * faceNormalsRy.y)
        faceNormalsRz.z = faceNormalsRy.z

        faceNormalsR.append(faceNormalsRz)

    return faceNormalsR

def v3_to_v2(v3points, offset):
    v2points = []
    for point in v3points:
        v2points.append(v2(point.x + offset.x, point.y + offset.y))
    return v2points

class Object:
    def hide_faces(self, cameraAngle):
        self.finalFaces = []
        for i in range(len(self.faces)):
            if self.faceNormalsR[i].dot(cameraAngle) > 0 and self.faces[i] not in self.finalFaces:
                self.finalFaces.append(self.faces[i])

    def __init__(self, pos, points, edges, faces, faceNormals, scale, rotation):
        self.pos = pos
        self.points = points
        self.edges = edges
        self.faces = faces
        self.faceNormals = faceNormals
        self.scale = scale
        self.rotation = rotation

    def tick(self, cameraAngle, cameraPosition,):
        self.pointsR = rotate_object(self.points, self.scale)
        self.faceNormalsR = rotate_normal(self.faceNormals, rot)

        translated = [p + self.pos for p in self.pointsR]
        self.v2points = v3_to_v2(translated, v2(0, 0))

        self.hide_faces(cameraAngle)

def create_object(filename, pos, scale, rotation):
    with open(filename, "r") as file:
        split1 = file.read().strip().split("/")
        points1 = [s for s in split1[0].split(";") if s]
        points = [v3(float(pointsList.split(",")[0]),float(pointsList.split(",")[1]),float(pointsList.split(",")[2])) for pointsList in points1]

        edges1 = [s for s in split1[1].split(";") if s]
        edges = [[int(edge) for edge in edgesList.split(",")] for edgesList in edges1]

        faces1 = [s for s in split1[2].split(";") if s]
        faces = [[int(face) for face in facesList.split(",")] for facesList in faces1]

        faceNormals1 = [s for s in split1[3].split(";") if s]
        faceNormals = [v3(float(faceNormalsList.split(",")[0]),float(faceNormalsList.split(",")[1]),float(faceNormalsList.split(",")[2])) for faceNormalsList in faceNormals1]

    obj = Object(pos, points, edges, faces, faceNormals, scale, rotation)
    objects.append(obj)

def rotate_keys(keyPressed, rotationOffset):
    if keyPressed[pygame.K_s]:
        rotationOffset.x -= rotationSpeed
    if keyPressed[pygame.K_w]:
        rotationOffset.x += rotationSpeed
    if keyPressed[pygame.K_a]:
        rotationOffset.y -= rotationSpeed
    if keyPressed[pygame.K_d]:
        rotationOffset.y += rotationSpeed
    if keyPressed[pygame.K_q]:
        rotationOffset.z -= rotationSpeed
    if keyPressed[pygame.K_e]:
        rotationOffset.z += rotationSpeed

    rotationOffset.x = math.remainder(rotationOffset.x,  2*pi)
    rotationOffset.y = math.remainder(rotationOffset.y,  2*pi)
    rotationOffset.z = math.remainder(rotationOffset.z,  2*pi)

    return rotationOffset

def move_keys(keyPressed, position):
    if keyPressed[pygame.K_s]:
        position.x -= moveSpeed
    if keyPressed[pygame.K_w]:
        position.x += moveSpeed
    if keyPressed[pygame.K_a]:
        position.y -= moveSpeed
    if keyPressed[pygame.K_d]:
        position.y += moveSpeed
    if keyPressed[pygame.K_q]:
        position.z -= moveSpeed
    if keyPressed[pygame.K_e]:
        position.z += moveSpeed

    position.x = math.remainder(position.x,  2*pi)
    position.y = math.remainder(position.y,  2*pi)
    position.z = math.remainder(position.z,  2*pi)

def draw_display():
    window.fill(BLACK)

    for obj in objects:
        for face in obj.finalFaces:
            for j in range(len(face)):
                start = obj.v2points[face[j]]
                end = obj.v2points[face[(j+1)%len(face)]]
                pygame.draw.line(window, WHITE, start, end, lineWidth)

def main():
    run = True
    clock = pygame.time.Clock()

    rotationOffset = v3(0,0,0)
    cameraPosition = v3(0,0,0)
    cameraAngle = v3(0,0,-1)

    create_object(os.path.join(script_dir, "cube.txt"), v3(WIDTH/2, HEIGHT/2, 0), 1.0, v3(0,0,0))

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        keyPressed = pygame.key.get_pressed()
        cameraAngle = rotate_keys(keyPressed, cameraAngle)
        cameraPosition = move_keys(keyPressed, cameraPosition)

        for obj in objects:
            obj.tick(cameraAngle, cameraPosition)

        draw_display()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
