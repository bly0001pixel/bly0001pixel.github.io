import pygame
from pygame import Vector2 as v2
pygame.init()

FPS, WIDTH, HEIGHT = 60, 700, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")

BLACK = (0,0,0)
WHITE = (255,255,255)

def draw_display():
    window.fill(BLACK)

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