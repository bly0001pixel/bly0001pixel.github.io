import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

FPS = 60
WIDTH = 1200
HEIGHT = 600

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Isometric")

BLACK = (0,0,0)
WHITE = (255,255,255)

#Handle Tiles
if True:
    Image_Tile_Grass = pygame.image.load(os.path.join("assets", "Grass.png")).convert_alpha()

    TileTypes = [None, Image_Tile_Grass]
    TileOffset = pygame.Vector2(45,22)

    def load_tiles(filename):
        file_map = open(filename)
        map_data = [[int(c) for c in row] for row in file_map.read().strip().split("\n")]
        file_map.close()
        return map_data

#Handle Player
if True:
    Image_Player_Idle = pygame.image.load(os.path.join("assets", "PlayerIdle.png")).convert_alpha()

    class Player:
        def __init__(self):
            self.position = pygame.Vector2(WIDTH/2-45/2,HEIGHT/2-40)
            self.image = Image_Player_Idle
            self.rect = pygame.Rect(self.position, self.image.get_size())
            self.speed = 3

    def handle_player_movement(keysPressed, player):
        delta = pygame.Vector2()

        if keysPressed[pygame.K_w]:
            delta.y += player.speed
        if keysPressed[pygame.K_s]:
            delta.y -= player.speed
        if keysPressed[pygame.K_d]:
            delta.x -= player.speed
        if keysPressed[pygame.K_a]:
            delta.x += player.speed

        player.position -= pygame.Vector2(delta.x * TileOffset, delta.y * TileOffset)
        player.rect.x, player.rect.y = player.position.x, player.position.y

def draw_game(map_data, player):
    window.fill(BLACK)
    
    for x, row in enumerate(map_data):
        for y, tile in enumerate(row):
            if tile != 0:
                window.blit(TileTypes[tile], (WIDTH/2-TileOffset.x+ ((y-x) * TileOffset.x), TileOffset.y*2 + ((y+x) * TileOffset.y)))

    window.blit(player.image, player.rect)

def main():
    clock = pygame.time.Clock()
    run = True

    player = Player()
    map_data = load_tiles("assets/map.txt")

    while run:
        clock.tick(FPS)
        keysPressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pass

            if event.type == pygame.KEYDOWN:
                MODS = pygame.key.get_mods()

                #Reload Map
                if event.key == pygame.K_l and MODS & pygame.KMOD_CTRL:
                        map_data = load_tiles("assets/map.txt")
                        print("Map Reloaded")

        handle_player_movement(keysPressed, player)

        draw_game(map_data, player)
        pygame.display.flip()

if __name__ == "__main__":

    main()