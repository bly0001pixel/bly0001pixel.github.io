import pygame as py
from pygame import Vector2 as v2

from settings import *
from physics import physics

py.init()
window = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Solar System Simulation")

bodies = []

camera_pos = v2(0, 0)
camera_speed = 300  # pixels per second
zoom = 1.0
zoom_speed = 0.1

class Body:
    def __init__(self, parameters):
        self.pos = parameters[0]
        self.vel = parameters[1] / scale  # Convert velocity to pixels/sec
        self.mass = parameters[2]         # Don't scale mass
        self.radius = max(1, parameters[3] / 10)
        self.colour = parameters[4]

def create_bodies():
    for parameters in bodies_parameters:
        body = Body(parameters)
        bodies.append(body)

def draw_display(bodies):
    window.fill(BLACK)
    for body in bodies:
        draw_pos = (body.pos - camera_pos) * zoom + v2(WIDTH / 2, HEIGHT / 2)
        py.draw.circle(window, body.colour, draw_pos, max(1, int(body.radius * zoom)))

def main():
    global camera_pos, zoom
    run = True
    clock = py.time.Clock()
    create_bodies()

    while run:
        dt = clock.tick(FPS) / 1000  # Delta time in seconds

        # --- Input Handling ---
        keys = py.key.get_pressed()
        move = v2(0, 0)
        if keys[py.K_w] or keys[py.K_UP]:
            move.y -= 1
        if keys[py.K_s] or keys[py.K_DOWN]:
            move.y += 1
        if keys[py.K_a] or keys[py.K_LEFT]:
            move.x -= 1
        if keys[py.K_d] or keys[py.K_RIGHT]:
            move.x += 1
        if move.length_squared() != 0:
            move = move.normalize()
        camera_pos += (move * camera_speed / zoom) * dt

        for event in py.event.get():
            if event.type == py.QUIT or (event.type == py.KEYDOWN and event.key == py.K_ESCAPE):
                run = False
            elif event.type == py.MOUSEWHEEL:
                zoom *= 1 + zoom_speed * event.y
                zoom = max(0.05, min(zoom, 10))  # clamp zoom range

        # --- Simulation ---
        physics(bodies, dt)

        # --- Drawing ---
        draw_display(bodies)
        py.display.flip()

    py.quit()

if __name__ == "__main__":
    main()