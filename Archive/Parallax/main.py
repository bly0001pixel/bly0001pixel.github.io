import pygame
import random
import math
pygame.init()

FPS, WIDTH, HEIGHT = 60, 1500, 1500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parallax")

BLACK = (0,0,0)
WHITE = (255,255,255)

stars = []
starNum = 200

mapSize = pygame.Vector3(10000,10000,10000)

cameraPos = pygame.Vector3(mapSize.x/2, mapSize.y/2, mapSize.z/2)
moveSpeed = 60
moveSpeedScale = 1
depthFactor = 300

cameraRotation = pygame.Vector3(0, 0, 0)

def rotate_vector(v, rotation):
    rx, ry, rz = rotation.x, rotation.y, rotation.z
    cosX, sinX = math.cos(rx), math.sin(rx)
    cosY, sinY = math.cos(ry), math.sin(ry)
    cosZ, sinZ = math.cos(rz), math.sin(rz)

    rot_matrix = [
        [cosY*cosZ, -cosY*sinZ, sinY],
        [sinX*sinY*cosZ + cosX*sinZ, -sinX*sinY*sinZ + cosX*cosZ, -sinX*cosY],
        [-cosX*sinY*cosZ + sinX*sinZ, cosX*sinY*sinZ + sinX*cosZ, cosX*cosY]
    ]

    return pygame.Vector3(
        v.x * rot_matrix[0][0] + v.y * rot_matrix[0][1] + v.z * rot_matrix[0][2],
        v.x * rot_matrix[1][0] + v.y * rot_matrix[1][1] + v.z * rot_matrix[1][2],
        v.x * rot_matrix[2][0] + v.y * rot_matrix[2][1] + v.z * rot_matrix[2][2]
    )

def move_relative_to_camera(direction):
    global cameraPos
    rotated_dir = rotate_vector(direction, cameraRotation)
    cameraPos += rotated_dir * moveSpeed

class Star():
    def calculate_spos(self):
        relPos = self.pos - cameraPos
        relPos = rotate_vector(relPos, cameraRotation)
        depth = relPos.z if relPos.z > 0 else 1
        scale = depthFactor / depth
        self.spos = pygame.Vector2(relPos.x * scale + WIDTH / 2, relPos.y * scale + HEIGHT / 2)
        self.size = max(2, int(self.original_size * scale))

    def __init__(self, pos, size):
        self.pos = pos
        self.original_size = size
        self.calculate_spos()

def create_star():
    stars.append(Star(pygame.Vector3(random.uniform(0, mapSize.x), random.uniform(0, mapSize.y), random.uniform(0, mapSize.z)), random.randint(5, 10)))

def start():
    for _ in range(starNum):
        create_star()

def draw_display():
    window.fill(BLACK)
    for star in stars:
        star.calculate_spos()
        pygame.draw.circle(window, WHITE, star.spos, star.size)

def main():
    clock = pygame.time.Clock()
    global moveSpeed, moveSpeedScale, cameraRotation
    start()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_relative_to_camera(pygame.Vector3(0,0,1))
                if event.key == pygame.K_s:
                    move_relative_to_camera(pygame.Vector3(0,0,-1))
                if event.key == pygame.K_a:
                    move_relative_to_camera(pygame.Vector3(-1,0,0))
                if event.key == pygame.K_d:
                    move_relative_to_camera(pygame.Vector3(1,0,0))
                if event.key == pygame.K_r:
                    move_relative_to_camera(pygame.Vector3(0,-1,0))
                if event.key == pygame.K_f:
                    move_relative_to_camera(pygame.Vector3(0,1,0))
                if event.key == pygame.K_UP:
                    cameraRotation.x -= math.radians(5)
                if event.key == pygame.K_DOWN:
                    cameraRotation.x += math.radians(5)
                if event.key == pygame.K_RIGHT:
                    cameraRotation.y -= math.radians(5)
                if event.key == pygame.K_LEFT:
                    cameraRotation.y += math.radians(5)
        draw_display()
        pygame.display.flip()

if __name__ == "__main__":
    main()