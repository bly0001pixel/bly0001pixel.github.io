import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

FPS = 60
WIDTH = 1280
HEIGHT = 640

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("")

BLACK = (0,0,0)
WHITE = (255,255,255)

#Handle Tiles
if True:
    TileSet_Image = pygame.image.load(os.path.join("assets", "TileSet.png")).convert_alpha()
    TileSet_ID = {0: pygame.Vector2(0,0), 1: pygame.Vector2(1,0)}
    Tile_Size = pygame.Vector2(64,64)

    TileMap1 = [
        [-1]*20,
        [-1]*20,
        [-1]*20,
        [-1]*20,
        [-1]*20,
        [-1]*20,
        [-1]*20,
        [-1]*20,
        [0]*20,
        [1]*20,
    ]

    def get_tile(TilePos):
        Tile_Rect = pygame.Rect(TilePos.x*Tile_Size.x, TilePos.y*Tile_Size.y, Tile_Size.x, Tile_Size.y)
        return TileSet_Image.subsurface(Tile_Rect)

    def render_tilemap(TileMap):
        for row in range(len(TileMap)):
            for col, id in enumerate(TileMap[row]):
                if id != -1:
                    tile = get_tile(TileSet_ID[id])
                    window.blit(tile, (col*Tile_Size.x, row*Tile_Size.y))

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        keysPressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pass

        render_tilemap(TileMap1)
        pygame.display.flip()

if __name__ == "__main__":
    main()