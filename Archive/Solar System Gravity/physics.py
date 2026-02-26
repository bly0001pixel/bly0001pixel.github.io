import math
from settings import gravity_constant

def gravity(i, j, bodies, dt):
    pos_i, pos_j = bodies[i].pos, bodies[j].pos
    diff = pos_j - pos_i
    dist = diff.length()

    if dist == 0:
        return

    force = gravity_constant * bodies[i].mass * bodies[j].mass / (dist ** 2)
    direction = diff.normalize()
    force_vector = direction * force

    bodies[i].vel += (force_vector / bodies[i].mass) * dt
    bodies[j].vel -= (force_vector / bodies[j].mass) * dt

def physics(bodies, dt):
    for i in range(len(bodies)):
        for j in range(i + 1, len(bodies)):
            gravity(i, j, bodies, dt)

    for body in bodies:
        body.pos += body.vel * dt